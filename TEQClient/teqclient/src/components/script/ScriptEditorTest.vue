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
});

const language = defineModel("language", { required: false, default: languages[0] });
const script = defineModel("script", { required: false, default: languages[0].script });

const testingResult = ref(null);

watch(
  () => props.testData,
  () => {
    testingResult.value = null;
  },
);

const run = () => {
  testingResult.value = null;

  return testPythonCode({
    script: script.value,
    unittests: props.testData.unittests,
    functionStructure: props.testData.functionStructure,
    functionType: props.testData.functionType,
  }).then((res) => {
    testingResult.value = res;
    console.log(res);
  });
};

const scriptOnChange = (lang) => {
  return lang.testFun;
};

const getFailure = (index) => {
  const fails = testingResult.value?.failures ?? [];

  return fails.find((fail) => extractNumber(fail.testName) === index);
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
            :test-name="`${$t('test')} #${index + 1}`"
            :failure="getFailure(index + 1)"
          ></UnittestResultItem>
        </div>
      </AceScriptEditor>
    </div>
  </div>
</template>

<style scoped></style>
