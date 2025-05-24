<script setup>

import TestItem from "@/components/test/TestItem.vue";
import {ref} from "vue";

const props = defineProps({
  item:{
    type: Object,
    required: true
  },
  index:{
    type: Number,
    required: true
  },
  title:{
    type: String,
    required: true
  },
  description:{
    type: String,
    required: true
  }
});

const item = ref(props.item);

const empty = ()=>{};
</script>

<template>
  <div class="col-12">
    <h2 class="tip-title">{{index}}. {{title}}</h2>
    <p>{{description}}</p>
  </div>
  <div class="col-12">
  <TestItem
    :on-item-paste="empty"
    :update-api="empty"
    :on-item-removed="empty"
    :auto-check="true"
    test-id="1"
    :index="index"
    v-model="item"
    :show-menu="false"/>
  </div>
</template>

<style scoped>

</style>
