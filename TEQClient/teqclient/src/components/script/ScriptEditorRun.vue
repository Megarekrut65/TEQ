<script setup>
import AceScriptEditor from "@/components/script/AceScriptEditor.vue";
import { languages } from "@/js/languages.js";
import { ref } from "vue";
import { runCode } from "@/js/api/microservices/runner.js";

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
const script = defineModel("script", { required: false, default: languages[0].script });

const output = ref(null);
const error = ref(null);

const run = (language, script) => {
  output.value = null;
  error.value = null;

  return runCode(language.type, script ?? "").then((res) => {
    output.value = res.output;
    error.value = res.error;
  });
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
      >
        <div v-if="output">
          <h2 class="my-0">{{ $t("output") }}</h2>
          <div>{{ output }}</div>
        </div>
        <div v-if="error" class="text-danger">
          {{ error }}
        </div>
      </AceScriptEditor>
    </div>
  </div>
</template>

<style scoped></style>
