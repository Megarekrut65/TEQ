<script setup>

import { ref } from "vue";
import { useRouter } from "vue-router";
import LoadingWindow from "@/components/LoadingWindow.vue";

import TestItemPass from "@/components/test/TestItemPass.vue";
import { MULTIPLE, SINGLE } from "@/js/types.js";
import { testPassPostApi } from "@/js/api/answer.js";
import { errorAlert } from "@/js/utility/utility.js";

const props = defineProps({
    instance: {
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

const answer = ref(props.answer?props.answer: {items: props.instance.items.map(createAnswerItem)});

const onSubmit = () => {
  loading.value = true;

  testPassPostApi(props.instance.id, answer.value).then(res=>{
    router.push({ name: "view", params: { answerId: res.id } });
  }).catch(errorAlert).finally(()=>{
    loading.value = false;
  });
};
</script>

<template>
    <LoadingWindow v-if="loading" />
    <div class="card">
      <div class="card-header bg-secondary">
        <h3 class="text-white">{{instance.title}}</h3>
      </div>
      <div class="card-body">
        {{instance.description}}
      </div>
    </div>

  <form @submit.prevent="onSubmit">


    <div class="mt-3 mb-3">
      <TestItemPass
        v-for="(item, index) in instance.items"
        :key="index"
        :index="index + 1"
        v-model="answer.items[index]"
        :item="item"
        :readonly="readonly"
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
