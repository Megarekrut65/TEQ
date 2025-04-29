<script setup>
import ScriptEditorRun from "@/components/script/ScriptEditorRun.vue";
import { ref } from "vue";
import { getLanguage } from "@/js/languages.js";

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
</script>

<template>
  <ScriptEditorRun
    language-readonly
    :readonly="readonly"
    v-model:language="language"
    v-model:script="formData.answer"
  ></ScriptEditorRun>
</template>

<style scoped></style>
