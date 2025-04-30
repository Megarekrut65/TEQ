<script setup>
import { ref } from "vue";
import { getLanguage } from "@/js/languages.js";
import AceScriptEditor from "@/components/script/AceScriptEditor.vue";

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
  <AceScriptEditor
    language-readonly
    :readonly="readonly"
    v-model:language="language"
    v-model:script="formData.answer"
  ></AceScriptEditor>
</template>

<style scoped></style>
