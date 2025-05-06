<script setup>
import SimilarityTool from "@/components/similarity/SimilarityTool.vue";
import { findTextSimilarity } from "@/js/api/microservices/ukrainian-similarity.js";

const findSimilarity = (text1, text2) => {
  return findTextSimilarity(text1, text2).then((res) => res.similarity);
};
</script>

<template>
  <SimilarityTool type="Text" :run-function="findSimilarity"></SimilarityTool>
</template>

<style scoped></style>
