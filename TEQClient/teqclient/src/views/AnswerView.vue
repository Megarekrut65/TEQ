<script setup>
import { useRoute } from "vue-router";
import { ref } from "vue";

import { errorAlert } from "@/js/utility/utility.js";
import LoadingWindow from "@/components/LoadingWindow.vue";
import TestPassForm from "@/components/pass/TestPassForm.vue";
import { answerGetApi } from "@/js/api/answer.js";

const { answerId } = useRoute().params;

const answer = ref(null);

const loading = ref(true);

answerGetApi(answerId)
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
