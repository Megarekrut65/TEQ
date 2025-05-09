<script setup>
import ace from "ace-builds/src-noconflict/ace";
import { onMounted, ref, watch } from "vue";
import { isDefaultScript, languages } from "@/js/languages.js";
import { errorAlert } from "@/js/utility/utility.js";

const props = defineProps({
  onRun: {
    type: Function,
    required: false,
  },
  scriptOnChange: {
    type: Function,
    required: false,
    default: (lang) => lang?.script ?? languages[0].testFun,
  },
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

const editorRef = ref(null);
const editor = ref(null);

const language = defineModel("language", { default: languages[0], required: true });
const script = defineModel("script", { required: true });

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

watch(language, (newValue) => {
  editor.value.session.setMode(getAceMode(newValue.ace));
  if (isDefaultScript(script.value)) {
    editor.value.session.setValue(props.scriptOnChange(newValue));
  }
});

onMounted(() => {
  editor.value = ace.edit(editorRef.value);
  editor.value.setTheme("ace/theme/dracula-css");
  editor.value.session.setMode(getAceMode(language.value.ace));

  editor.value.session.setValue(script.value ?? props.scriptOnChange(language.value));

  editor.value.setReadOnly(props.readonly);

  editor.value.session.on("change", () => {
    script.value = editor.value.getValue();
    props.onChanged();
  });
});

const ran = ref(false);

const run = () => {
  ran.value = true;

  props
    .onRun(language.value, script.value ?? "")
    .catch(errorAlert)
    .finally(() => {
      ran.value = false;
    });
};
</script>

<template>
  <div class="card">
    <div class="card-header">
      <div class="input-group mb-3">
        <label class="input-group-text mb-0">{{ $t("language") }}</label>
        <select
          class="form-select mb-0"
          v-model="language"
          :disabled="languageReadonly || readonly"
        >
          <option v-for="lang in languages" :key="lang" :value="lang" selected>
            {{ lang.name }}
          </option>
        </select>
        <button
          class="btn btn-outline-secondary my-0"
          type="button"
          @click="run"
          :disabled="ran || readonly || script.length === 0"
        >
          {{ $t("run") }}
        </button>
      </div>
    </div>
    <div class="card-body">
      <div ref="editorRef" class="editor"></div>
    </div>
    <div class="card-footer"><slot></slot></div>
  </div>
</template>

<style scoped>
.editor {
  height: 300px;
  position: relative;
}
.card-footer {
  white-space: pre-wrap;
  max-height: 200px;
  overflow-y: auto;
}
</style>
