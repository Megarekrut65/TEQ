<script setup>

import { useRoute } from "vue-router";
import { ref } from "vue";
import { testViewGetApi } from "@/js/api/answer.js";
import { errorAlert } from "@/js/utility/utility.js";
import LoadingWindow from "@/components/LoadingWindow.vue";
import TestPassForm from "@/components/test/TestPassForm.vue";

const { testId } = useRoute().params;

const test = ref(null);

const loading = ref(true);

testViewGetApi(testId).then((res) => {
  test.value = res;
}).catch(errorAlert).finally(() => {
  loading.value = false;
});

</script>

<template>
  <LoadingWindow v-if="loading" />
  <TestPassForm v-if="test" :instance="test"/>
</template>

<style scoped>

</style>
