<script setup>

import AceScriptEditor from "@/components/script/AceScriptEditor.vue";
import { languages } from "@/js/languages.js";

const language = defineModel("language", {required: false, default: languages[0]});
const script = defineModel("script", {required: false});

const run = (language, script)=>{

  const runner = language.runner;
  return runner(script ?? "");
};
</script>

<template>
  <div class="row">
    <div class="col-12">

    <AceScriptEditor :on-run="run" v-model:language="language" v-model:script="script"></AceScriptEditor>
    </div>
  </div>
</template>

<style scoped>

</style>
