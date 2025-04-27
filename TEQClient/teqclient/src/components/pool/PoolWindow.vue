<script setup>


import ModalWindow from "@/components/ModalWindow.vue";
import { ref, watch } from "vue";
import { itemCreateApi, poolGetApi } from "@/js/api/pool.js";
import { errorAlert } from "@/js/utility/utility.js";

const model = defineModel({default: false});
const item = defineModel("item");

const pool = ref(null);

poolGetApi().then(res=>{
  pool.value = res;
}).catch(errorAlert);

const createCategory = ()=>{

};

const added = ref(new Set());
watch(item, ()=>added.value.clear());

const addToPool = (category)=>{
  itemCreateApi(category.id, item.value).catch(errorAlert);
  added.value.add(category.id);
};

</script>

<template>
<ModalWindow v-model="model" size="medium">
  <template v-slot:header>
    <h3 class="my-0">{{$t('pool')}} <a href="#" @click="createCategory"><i class="fa fa-plus"></i></a></h3>
  </template>
  <div v-if="pool" class="pool">
    <div v-for="category in pool.categories" :key="category" class="card  mt-1">
      <div class="card-body d-flex justify-content-between">
        <div>{{category.name}}</div>
        <div class="btn-hover" @click="()=>addToPool(category)" v-if="!added.has(category.id)"><i class="fa fa-plus"></i></div>
      </div>
    </div>
  </div>

</ModalWindow>
</template>

<style scoped>
.pool{
  max-height: 60vh;
  overflow-y: auto;
}

</style>
