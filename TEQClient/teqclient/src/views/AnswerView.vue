<script setup>

import { useRoute } from "vue-router";
import { ref } from "vue";
import { answerGetApi } from "@/js/api/answer.js";
import { errorAlert } from "@/js/utility/utility.js";
import LoadingWindow from "@/components/LoadingWindow.vue";
import TestPassForm from "@/components/test/TestPassForm.vue";

const { answerId } = useRoute().params;

const answer = ref(null);

const loading = ref(true);

answerGetApi(answerId).then((res) => {
  answer.value = res;
}).catch(errorAlert).finally(() => {
  loading.value = false;
});

</script>

<template>
  <LoadingWindow v-if="loading" />
  <TestPassForm v-if="answer" :instance="answer.test" :answer="answer" :readonly="true"/>
</template>

<style scoped>

</style>
