<script setup>
import { ref } from "vue";
import ScriptEditorRun from "@/components/script/ScriptEditorRun.vue";
import ScriptUnittestAnswer from "@/components/test/items/ScriptUnittestAnswer.vue";

const toolTypes = ["runCode", "testCode", "similarityCode", "similarityText"];
const tool = ref(toolTypes[0]);
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-header">
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
          </div>

          <div class="card-body">
            <div v-if="tool === 'runCode'">
              <ScriptEditorRun />
            </div>
            <div v-else-if="tool === 'testCode'">
              <ScriptUnittestAnswer />
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
