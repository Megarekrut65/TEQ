<script setup>
import { ref } from "vue";
import ScriptSimilarityTool from "@/components/tools/ScriptSimilarityTool.vue";
import TextSimilarityTool from "@/components/tools/TextSimilarityTool.vue";
import RunTestTool from "@/components/tools/RunTestTool.vue";
import RunCodeTool from "@/components/tools/RunCodeTool.vue";

const toolTypes = ["runCode", "testCode", "similarityCode", "similarityText"];
const tool = ref(toolTypes[0]);
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
              <RunCodeTool />
            </div>
            <div v-else-if="tool === 'testCode'">
              <RunTestTool />
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
