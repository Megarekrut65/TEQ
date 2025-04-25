<script setup>

import { useRoute } from "vue-router";
import { ref } from "vue";
import LoadingWindow from "@/components/LoadingWindow.vue";
import NotFoundImage from "@/components/NotFoundImage.vue";
import CategoryForm from "@/components/pool/CategoryForm.vue";
import { categoryGetApi } from "@/js/api/pool.js";

const { categoryId } = useRoute().params;

const category = ref(null);

const loading = ref(true);
const notFound = ref(false);

categoryGetApi(categoryId).then((res) => {
  category.value = res;
}).catch((err)=>{
  console.log(err);
  notFound.value = true;
}).finally(() => {
  loading.value = false;
});

</script>

<template>
  <LoadingWindow v-if="loading" />
  <CategoryForm v-if="category" :instance="category" />
  <NotFoundImage v-if="notFound"></NotFoundImage>
</template>

<style scoped>

</style>
