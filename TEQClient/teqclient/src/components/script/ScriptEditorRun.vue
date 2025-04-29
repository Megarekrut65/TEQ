<script setup>
import AceScriptEditor from "@/components/script/AceScriptEditor.vue";
import { languages } from "@/js/languages.js";

defineProps({
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
});

const language = defineModel("language", { required: false, default: languages[0] });
const script = defineModel("script", { required: false });

const run = (language, script) => {
  const runner = language.runner;
  return runner(script ?? "");
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
      ></AceScriptEditor>
    </div>
  </div>
</template>

<style scoped></style>
