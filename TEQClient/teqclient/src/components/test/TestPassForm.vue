<script setup>

import { ref } from "vue";
import { useRouter } from "vue-router";
import LoadingWindow from "@/components/LoadingWindow.vue";

import TestItemPass from "@/components/test/TestItemPass.vue";
import { MULTIPLE, SINGLE } from "@/js/types.js";

const props = defineProps({
    instance: {
        type: Object,
        required: true
    },
    readonly: {
        type: Boolean,
        required: false,
        default: false
    },
});

const router = useRouter();

const loading = ref(false);

const onSubmit = () => {
    loading.value = true;

    console.log(answer)
};

const createChoices = (type)=>{
  if(type===SINGLE) return [-1];
  if(type===MULTIPLE) return [];

  return null;
};

const createAnswerItem = (item)=>{
  return {
    choices: createChoices(item.type),
    answer:""
  };
};

const answer = ref({items: props.instance.items.map(createAnswerItem)});
console.log(answer)

</script>

<template>
    <LoadingWindow v-if="loading" />
    <div class="card">
      <div class="card-header">
        <h3>{{instance.title}}</h3>
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

    <button type="submit" class="btn btn-outline-success">{{$t('submit')}}</button>
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
