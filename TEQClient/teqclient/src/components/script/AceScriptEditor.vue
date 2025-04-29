<script setup>
import ace from "ace-builds/src-noconflict/ace";
import { onMounted, ref, watch } from "vue";
import { languages } from "@/js/languages.js";
import { errorAlert } from "@/js/utility/utility.js";

const props = defineProps({
  onRun: {
    type: Function,
    required: false,
  },
  scriptOnChange: {
    type: Function,
    required: false,
    default: (lang) => lang.script,
  },
});

const editor = ref(null);

const language = defineModel("language", { default: languages[0], required: true });
const script = defineModel("script", { default: "" });
const output = ref(null);
const error = ref(null);

const getAceMode = (lang) => {
  const mode = `ace/mode/${lang.toLowerCase()}`;
  try {
    ace.require(mode);
    return mode;
    // eslint-disable-next-line no-unused-vars
  } catch (e) {
    return "ace/mode/text";
  }
};

watch(language, () => {
  editor.value.session.setMode(getAceMode(language.value.ace));
  editor.value.session.setValue(props.scriptOnChange(language.value));
});

watch(script, () => {
  if (script.value === editor.value.getValue()) return;

  editor.value.session.setValue(script.value ?? language.value.script);
});

onMounted(() => {
  editor.value = ace.edit("editor");
  editor.value.setTheme("ace/theme/dracula-css");
  editor.value.session.setMode(getAceMode(language.value.ace));

  editor.value.session.setValue(script.value ?? props.scriptOnChange(language.value));

  editor.value.session.on("change", () => {
    if (script.value === editor.value.getValue()) return;

    script.value = editor.value.getValue();
  });
});

const run = () => {
  output.value = null;
  error.value = null;

  props
    .onRun(language.value, script.value ?? "")
    .then((res) => {
      output.value = res.output;
      error.value = res.error;
    })
    .catch(errorAlert);
};
</script>

<template>
  <div class="card">
    <div class="card-header">
      <div class="input-group mb-3">
        <label class="input-group-text mb-0" for="inputGroupSelect01">{{ $t("language") }}</label>
        <select class="form-select mb-0" id="inputGroupSelect01" v-model="language">
          <option v-for="lang in languages" :key="lang" :value="lang" selected>
            {{ lang.name }}
          </option>
        </select>
        <button class="btn btn-outline-secondary my-0" type="button" @click="run">
          {{ $t("run") }}
        </button>
      </div>
    </div>
    <div class="card-body">
      <div id="editor"></div>
    </div>
    <div class="card-footer" v-if="output || error">
      <div v-if="output">
        <h2 class="my-0">{{ $t("output") }}</h2>
        <div>{{ output }}</div>
      </div>
      <div v-if="error" class="text-danger">
        {{ error }}
      </div>
    </div>
  </div>
</template>

<style scoped>
#editor {
  height: 300px;
  position: relative;
}
.card-footer {
  white-space: pre-wrap;
  max-height: 200px;
  overflow-y: auto;
}
</style>
