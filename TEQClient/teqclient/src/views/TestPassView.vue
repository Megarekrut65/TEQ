<script setup>

import { useRoute } from "vue-router";
import { ref } from "vue";
import { testPassGetApi } from "@/js/api/answer.js";
import LoadingWindow from "@/components/LoadingWindow.vue";
import TestPassForm from "@/components/test/TestPassForm.vue";
import NotFoundImage from "@/components/NotFoundImage.vue";

const { testId } = useRoute().params;

const test = ref(null);

const loading = ref(true);
const notFound = ref(false);

testPassGetApi(testId).then((res) => {
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
  <TestPassForm v-if="test" :test="test"/>
  <NotFoundImage v-if="notFound"></NotFoundImage>
</template>

<style scoped>

</style>
