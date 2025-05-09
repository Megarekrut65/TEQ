<script setup>
import SimilarityTool from "@/components/tools/SimilarityTool.vue";
import { findScriptSimilarity } from "@/js/api/microservices/pl-similarity.js";

const findSimilarity = (code1, code2) => {
  return findScriptSimilarity(code1, code2).then((res) => res.similarity);
};
</script>

<template>
  <SimilarityTool type="Code" :run-function="findSimilarity"></SimilarityTool>
</template>

<style scoped></style>
