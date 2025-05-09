<script setup>
import { defaultUnitTests } from "@/js/data-types.js";
import { ref, watch } from "vue";
import ScriptUnittestAnswer from "@/components/test/items/ScriptUnittestAnswer.vue";
import { languages } from "@/js/languages.js";
import { RETURN_TYPES } from "@/js/types.js";

const getTests = (prefix) => {
  const json = localStorage.getItem(`${prefix}-tests`);
  if (json) {
    try {
      return JSON.parse(json);
      // eslint-disable-next-line no-unused-vars
    } catch (err) {
      /* empty */
    }
  }

  return defaultUnitTests(prefix);
};

const getTestObject = () => {
  const json = localStorage.getItem("test-object");
  if (json) {
    try {
      return JSON.parse(json);
      // eslint-disable-next-line no-unused-vars
    } catch (err) {
      /* empty */
    }
  }

  return {
    language: languages[0].type,
    functionType: RETURN_TYPES[0],
    functionStructure: languages[0].testFunStruct,
    script: languages[0].testFun,
  };
};

const setTests = (prefix, tests) => {
  localStorage.setItem(`${prefix}-tests`, JSON.stringify(tests));
};

const setTestObject = (obj) => {
  localStorage.setItem("test-object", JSON.stringify(obj));
};

const publicUnittests = ref(getTests("public"));
const privateUnittests = ref(getTests("private"));
const testObject = ref(getTestObject());

watch(
  testObject,
  () => {
    setTestObject(testObject.value);
  },
  { deep: true },
);

watch(
  publicUnittests,
  () => {
    setTests("public", publicUnittests.value);
  },
  { deep: true },
);

watch(
  privateUnittests,
  () => {
    setTests("private", privateUnittests.value);
  },
  { deep: true },
);
</script>

<template>
  <ScriptUnittestAnswer
    v-model:private-unittests="privateUnittests"
    v-model:public-unittests="publicUnittests"
    v-model="testObject"
    v-model:script="testObject.script"
  />
</template>

<style scoped></style>
