<script setup>
import { useRoute } from "vue-router";
import { ref } from "vue";
import { answerLastGetApi } from "@/js/api/answer.js";
import { errorAlert } from "@/js/utility/utility.js";
import LoadingWindow from "@/components/LoadingWindow.vue";
import TestPassForm from "@/components/pass/TestPassForm.vue";

const { testId } = useRoute().params;

const answer = ref(null);

const loading = ref(true);

answerLastGetApi(testId)
  .then((res) => {
    answer.value = res;
  })
  .catch(errorAlert)
  .finally(() => {
    loading.value = false;
  });
</script>

<template>
  <LoadingWindow v-if="loading" />
  <div class="container">
    <TestPassForm v-if="answer" :test="answer.test" :answer="answer" :readonly="true" />
  </div>
</template>

<style scoped></style>
