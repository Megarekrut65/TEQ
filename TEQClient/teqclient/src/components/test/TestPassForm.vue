<script setup>

import { ref } from "vue";
import { useRouter } from "vue-router";
import LoadingWindow from "@/components/LoadingWindow.vue";

import TestItemPass from "@/components/test/TestItemPass.vue";
import { MULTIPLE, SINGLE } from "@/js/types.js";
import { testPassPostApi } from "@/js/api/answer.js";
import { errorAlert } from "@/js/utility/utility.js";

const props = defineProps({
    test: {
        type: Object,
        required: true
    },
    answer:{
        type: Object,
        required: false,
        default: null
    },
    readonly: {
        type: Boolean,
        required: false,
        default: false
    },
});

const router = useRouter();

const loading = ref(false);

const createChoices = (type)=>{
  if(type===SINGLE) return [-1];
  if(type===MULTIPLE) return [];

  return null;
};

const createAnswerItem = (item)=>{
  return {
    type: item.type,
    choices: createChoices(item.type),
    answer:""
  };
};

const answer = ref(props.answer?props.answer: {items: props.test.items.map(createAnswerItem), testItems:props.test.items});

console.log(answer)

const onSubmit = () => {
  loading.value = true;

  testPassPostApi(props.test.id, answer.value).then(()=>{
    router.push({ name: "view", params: { testId: props.test.id } });
  }).catch(errorAlert).finally(()=>{
    loading.value = false;
  });
};
</script>

<template>
    <LoadingWindow v-if="loading" />
    <div class="card">
      <div class="card-header bg-secondary d-flex justify-content-between">
        <h3 class="text-white">{{ test.title }}</h3>

        <div>
          <span v-if="answer.checked" class="badge text-dark bg-primary me-2">{{ answer.grade }}/{{ answer.maxGrade }}</span>
          <span v-if="answer.checked" class="badge text-dark bg-info me-2">{{$t('checked')}}</span>
          <span v-if="answer.autoChecked" class="badge text-dark bg-warning">{{$t('autoChecked')}}</span>
        </div>

      </div>
      <div class="card-body" v-if="test.description">
        {{ test.description }}
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
        :show-correct="test.showCorrect && readonly && answer.checked"
        :auto-check="answer.autoChecked"
      />
    </div>

    <button v-if="!readonly" type="submit" class="btn btn-outline-success">{{$t('submit')}}</button>
  </form>
</template>

<style scoped>
button {
    margin: 0;
}

form {
    margin-bottom: 0;
}
</style>
