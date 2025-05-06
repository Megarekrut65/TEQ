<script setup>
import { ref } from "vue";
import ScriptEditorRun from "@/components/script/ScriptEditorRun.vue";
import ScriptUnittestAnswer from "@/components/test/items/ScriptUnittestAnswer.vue";
import ScriptSimilarityTool from "@/components/similarity/ScriptSimilarityTool.vue";
import TextSimilarityTool from "@/components/similarity/TextSimilarityTool.vue";
import { defaultUnitTests } from "@/js/data-types.js";

const toolTypes = ["runCode", "testCode", "similarityCode", "similarityText"];
const tool = ref(toolTypes[0]);

const publicUnittests = ref(defaultUnitTests("public"));
const privateUnittests = ref(defaultUnitTests("private"));
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <ul class="nav nav-tabs">
              <li class="nav-item" v-for="type in toolTypes" :key="type">
                <div
                  :class="{ 'nav-link btn-hover': true, active: type === tool }"
                  aria-current="page"
                  @click="tool = type"
                >
                  {{ $t(type) }}
                </div>
              </li>
            </ul>
            <div v-if="tool === 'runCode'">
              <ScriptEditorRun />
            </div>
            <div v-else-if="tool === 'testCode'">
              <ScriptUnittestAnswer
                v-model:private-unittests="privateUnittests"
                v-model:public-unittests="publicUnittests"
              />
            </div>
            <div v-else-if="tool === 'similarityCode'">
              <ScriptSimilarityTool />
            </div>
            <div v-else-if="tool === 'similarityText'">
              <TextSimilarityTool />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
img {
  width: 100%;
}
</style>
