<script setup>
import { ref } from "vue";
import { getLanguage } from "@/js/languages.js";
import ScriptEditorTest from "@/components/script/ScriptEditorTest.vue";
import UnittestItem from "@/components/test/items/UnittestItem.vue";

const props = defineProps({
  readonly: {
    type: Boolean,
    required: true,
  },
  item: {
    type: Object,
    required: true,
  },
});

const language = ref(getLanguage(props.item.language));
const formData = defineModel({ required: true });

const testData = ref({
  functionStructure: props.item.functionStructure,
  functionType: props.item.functionType,
  unittests: props.item.publicUnittests.concat(props.item.privateUnittests ?? []),
});

const testResult = ref(
  formData.value.failures !== undefined
    ? {
        failures: formData.value.failures,
        totalTests: formData.value.totalTests,
        passed: formData.value.passed,
      }
    : null,
);
</script>

<template>
  <div class="row">
    <div class="col-12 col-md-8">
      <ScriptEditorTest
        v-model:language="language"
        v-model:script="formData.answer"
        :key="formData.type"
        :test-data="testData"
        language-readonly
        :readonly="readonly"
        :test-result="testResult"
      >
      </ScriptEditorTest>
    </div>
    <div class="col-12 col-md-4 mt-2 mt-md-0">
      <h2 class="mt-0">{{ $t("tests") }}</h2>
      <UnittestItem
        v-for="(unit, index) in testData.unittests"
        :key="unit"
        v-model="testData.unittests[index]"
        :index="index"
        :count="0"
        :on-removed="() => {}"
        readonly
      />
    </div>
  </div>
</template>

<style scoped></style>
