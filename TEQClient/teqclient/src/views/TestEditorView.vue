<script setup>

import TestForm from "@/components/test/TestForm.vue";
import { useRoute } from "vue-router";
import { ref } from "vue";
import { testGetApi } from "@/js/api/test.js";
import LoadingWindow from "@/components/LoadingWindow.vue";
import NotFoundImage from "@/components/NotFoundImage.vue";

const { testId } = useRoute().params;

const test = ref(null);

const loading = ref(true);
const notFound = ref(false);

testGetApi(testId).then((res) => {
  test.value = res;
}).catch((err)=>{
  console.log(err);
  notFound.value = true;
}).finally(() => {
  loading.value = false;
});

</script>

<template>
  <LoadingWindow v-if="loading" />
  <TestForm v-if="test" :instance="test" />
  <NotFoundImage v-if="notFound"></NotFoundImage>
</template>

<style scoped>

</style>
