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

testGetApi(testId).then((res) => {
  test.value = res;
}).catch((err)=>{
  console.log(err);
}).finally(() => {
  loading.value = false;
});

</script>

<template>
  <LoadingWindow v-if="loading" />
  <TestForm v-if="test" :instance="test" mode="update" />
  <NotFoundImage v-else></NotFoundImage>
</template>

<style scoped>

</style>
