<script setup>
import { ref, watch } from "vue";
import { getLanguage, languages } from "@/js/languages.js";
import ScriptEditorRun from "@/components/script/ScriptEditorRun.vue";

const getRunObject = () => {
  const json = localStorage.getItem("run-object");
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
    script: languages[0].script,
  };
};

const setRunObject = (obj) => {
  localStorage.setItem("run-object", JSON.stringify(obj));
};

const runObject = ref(getRunObject());

watch(
  runObject,
  () => {
    setRunObject(runObject.value);
  },
  { deep: true },
);

const language = ref(getLanguage(runObject.value.language));
watch(language, () => {
  runObject.value.language = language.value.type;
});
</script>

<template>
  <ScriptEditorRun v-model:script="runObject.script" v-model:language="language" />
</template>

<style scoped></style>
