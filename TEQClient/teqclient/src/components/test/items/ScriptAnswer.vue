<script setup>

import ScriptEditorRun from "@/components/script/ScriptEditorRun.vue";
import { ref, watch } from "vue";
import { getLanguage } from "@/js/languages.js";

const formData = defineModel({required:true});

const language = ref(getLanguage(formData.value.language));

watch(language, ()=>{
  formData.value.language = language.value?.type;
});
</script>

<template>
  <div  class="mb-3">
    <label for="correctAnswer" class="form-label">{{ $t("correctAnswer") }}</label>
    <ScriptEditorRun v-model:language="language" v-model:script="formData.correctAnswer"></ScriptEditorRun>
  </div>
</template>

<style scoped>

</style>
