<script setup>

import TestForm from "@/components/test/TestForm.vue";
import { useRoute } from "vue-router";
import { ref } from "vue";
import { testGetApi } from "@/js/api/test.js";
import { errorAlert } from "@/js/utility/utility.js";
import LoadingWindow from "@/components/LoadingWindow.vue";

const { testId } = useRoute().params;

const test = ref(null);

const loading = ref(true);

testGetApi(testId).then((res) => {
  test.value = res;
}).catch(errorAlert).finally(() => {
  loading.value = false;
});

</script>

<template>
  <LoadingWindow v-if="loading" />
  <TestForm v-if="test" :instance="test" mode="update" />
</template>

<style scoped>

</style>
