<script setup>
import SimilarityTool from "@/components/tools/SimilarityTool.vue";
import { findTextSimilarity } from "@/js/api/microservices/nl-similarity.js";

const findSimilarity = (text1, text2) => {
  return findTextSimilarity(text1, text2).then((res) => res.similarity);
};
</script>

<template>
  <SimilarityTool type="Text" :run-function="findSimilarity"></SimilarityTool>
</template>

<style scoped></style>
