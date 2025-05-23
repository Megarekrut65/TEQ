<script setup>
import {ref, watch} from "vue";
import { useRouter } from "vue-router";
import LoadingWindow from "@/components/LoadingWindow.vue";

import TestItemPass from "@/components/pass/TestItemPass.vue";
import { MULTIPLE, SCRIPT_UNITTEST, SINGLE } from "@/js/types.js";
import { answerAgreeUpdateApi, answerCheckUpdateApi, testPassPostApi } from "@/js/api/answer.js";
import { errorAlert } from "@/js/utility/utility.js";
import { getUser } from "@/js/utility/auth.js";

const props = defineProps({
  test: {
    type: Object,
    required: true,
  },
  answer: {
    type: Object,
    required: false,
    default: null,
  },
  readonly: {
    type: Boolean,
    required: false,
    default: false,
  },
});

const router = useRouter();

const loading = ref(false);

const createChoices = (type) => {
  if (type === SINGLE) return [-1];
  if (type === MULTIPLE) return [];

  return null;
};

const createAnswerItem = (item) => {
  const text = item.type === SCRIPT_UNITTEST ? item.functionStructure : "";

  return {
    type: item.type,
    choices: createChoices(item.type),
    answer: text,
  };
};

const answer = ref(
  props.answer
    ? props.answer
    : { items: props.test.items.map(createAnswerItem), testItems: props.test.items },
);

if(!props.answer){
  const savedAnswer = localStorage.getItem(props.test.id);
  if (savedAnswer) {
    try{
      answer.value = JSON.parse(savedAnswer);
      // eslint-disable-next-line no-unused-vars
    } catch(error) { /* empty */ }

  }

  watch(()=>answer, ()=>{
    localStorage.setItem(props.test.id, JSON.stringify(answer.value));
  }, {deep: true});
}


const onSubmit = () => {
  loading.value = true;

  testPassPostApi(props.test.id, answer.value)
    .then(() => {
      router.push({ name: "view", params: { testId: props.test.id } });
    })
    .catch(errorAlert)
    .finally(() => {
      loading.value = false;
      localStorage.removeItem(props.test.id);
    });
};

const userIsTestOwner = () => {
  const user = getUser();
  if (user) return user.id === props.answer?.test?.owner?.id;
  return false;
};
const isTestOwner = ref(userIsTestOwner());

const userIsAnswerOwner = () => {
  const user = getUser();
  if (user) return user.id === props.answer?.owner?.id && answer.value?.id;
  return false;
};
const isAnswerOwner = ref(userIsAnswerOwner());

const markChecked = () => {
  answerCheckUpdateApi(answer.value.id)
    .then(() => {
      answer.value.checked = true;
    })
    .catch(errorAlert);
};

const markAgree = () => {
  answerAgreeUpdateApi(answer.value.id)
    .then(() => {
      answer.value.agree = true;
    })
    .catch(errorAlert);
};

const updateGrade = () => {
  let grade = 0;
  for (let item of answer.value.items) {
    grade += item.grade;
  }

  answer.value.grade = grade;
};

const refresh = () => {
  window.location.reload();
};
</script>

<template>
  <LoadingWindow v-if="loading" />
  <div class="card">
    <div class="card-header bg-secondary">
      <div class="row">
        <h3 class="text-white col-12 col-md-6">
          <span class="btn-hover" v-if="answer?.id && answer?.checked === false"
            ><i class="fa-solid fa-arrows-rotate" @click="refresh"></i
          ></span>
          {{ test.title }}
        </h3>

        <div class="text-primary text-right col-12 col-md-6" v-if="answer?.id">
          <div>{{ answer.owner.fullname }}</div>
          <div>{{ answer.owner.email }}</div>
        </div>
        <div class="col-12 mt-2" v-if="answer.id">
          <span v-if="answer.checked || isTestOwner" class="badge text-dark bg-primary me-2"
            >{{ answer.grade }}/{{ answer.maxGrade }}</span
          >
          <span v-if="answer.checked" class="badge text-dark bg-info me-2">
            {{ $t("checked") }}</span
          >
          <span v-else class="badge text-dark bg-info me-2"> {{ $t("checking") }}</span>

          <span v-if="answer.autoChecked" class="badge text-dark bg-warning me-2">
            {{ $t("autoChecked") }}</span
          >
          <span v-if="!answer.agree && answer.checked" class="badge text-dark bg-danger">{{ $t("notAgreed") }}</span>
        </div>
      </div>
    </div>
    <div class="card-body">
      {{ test.description }}
    </div>

    <div class="card-footer" v-if="answer.id">
      <button
        v-if="isTestOwner"
        :disabled="answer.checked"
        class="btn btn-success"
        @click="markChecked"
      >
        {{ $t("markChecked") }}
      </button>
      <button
        v-if="isAnswerOwner && answer.checked"
        :disabled="answer.agree"
        class="btn btn-danger ms-2"
        @click="markAgree"
      >
        {{ $t("markAgree") }}
      </button>
    </div>
  </div>

  <form @submit.prevent="onSubmit">
    <div class="mt-3 mb-3">
      <TestItemPass
        v-for="(item, index) in answer.testItems"
        :key="index"
        :index="index + 1"
        v-model="answer.items[index]"
        :item="item"
        :readonly="readonly"
        :show-correct="(test.showCorrect && readonly && answer.checked) || isTestOwner"
        :auto-check="answer.autoChecked && answer.checked"
        :answer-id="answer.id ?? ''"
        :is-owner="isTestOwner"
        :update-grade="updateGrade"
      />
    </div>

    <button v-if="!readonly" type="submit" class="btn btn-outline-success">
      {{ $t("submit") }}
    </button>
  </form>
</template>

<style scoped>
button {
  margin: 0;
}

form {
  margin-bottom: 0;
}
span.btn-hover:hover {
  color: black;
}
</style>
