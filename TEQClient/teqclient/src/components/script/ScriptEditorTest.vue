<script setup>
import AceScriptEditor from "@/components/script/AceScriptEditor.vue";
import { languages } from "@/js/languages.js";
import { testPythonCode } from "@/js/api/microservices/python-tester.js";
import { ref, watch } from "vue";
import UnittestResultItem from "@/components/script/UnittestResultItem.vue";
import { extractNumber } from "@/js/utility/utility.js";

const props = defineProps({
  readonly: {
    type: Boolean,
    required: false,
    default: false,
  },
  languageReadonly: {
    type: Boolean,
    required: false,
    default: false,
  },
  onChanged: {
    type: Function,
    required: false,
    default: () => {},
  },
  testData: {
    type: Object,
    required: true,
  },
  testResult: {
    type: Object,
    required: false,
    default: null,
  },
});

const language = defineModel("language", { required: false, default: languages[0] });
const script = defineModel("script", { required: true });

const testingResult = ref(props.testResult);
const error = ref(null);

watch(
  () => props.testData,
  () => {
    testingResult.value = null;
    error.value = null;
  },
);

const run = () => {
  testingResult.value = null;
  error.value = null;

  return testPythonCode({
    script: script.value,
    unittests: props.testData.unittests,
    functionStructure: props.testData.functionStructure,
    functionType: props.testData.functionType,
  }).then((res) => {
    if ("status_code" in res && res.status_code !== 200) {
      error.value = res.detail;
      return;
    }

    testingResult.value = res;
    console.log(res);
  });
};

const scriptOnChange = (lang) => {
  if (lang) return lang.testFun;

  return languages[0].testFun;
};
const getName = (fail, index) => {
  if (fail.testPrefix) return `${fail.testPrefix}${index}`;
  return `${index}`;
};

const getFailure = (index) => {
  const fails = testingResult.value?.failures ?? [];

  return fails.find((fail) => `${extractNumber(fail.testName)}` === getName(fail, index)) ?? null;
};
</script>

<template>
  <div class="row">
    <div class="col-12">
      <AceScriptEditor
        :on-run="run"
        v-model:language="language"
        v-model:script="script"
        :readonly="readonly"
        :language-readonly="languageReadonly"
        :on-changed="onChanged"
        :script-on-change="scriptOnChange"
      >
        <div v-if="testingResult">
          <UnittestResultItem
            v-for="(test, index) in testData.unittests"
            :key="test"
            :test-name="`${$t(test.prefix)} ${$t('test')} #${index + 1}`"
            :failure="getFailure(index + 1)"
          ></UnittestResultItem>
        </div>

        <div v-if="error" class="error text-danger">
          {{ error }}
        </div>
      </AceScriptEditor>
    </div>
  </div>
</template>

<style scoped>
.error {
  white-space: pre-wrap;
}
</style>
