<script setup>
import { ref } from "vue";
import { publicTestListApi } from "@/js/api/test.js";
import { errorAlert } from "@/js/utility/utility.js";
import PublicTestCard from "@/components/test/PublicTestCard.vue";

const tests = ref([]);


publicTestListApi()
    .then((res) => {
        tests.value = res.results;
        console.log(res);
    })
    .catch(errorAlert);

</script>

<template>
   <div>
      <div class="row">
        <PublicTestCard v-for="test in tests" :key="test.id" :test="test"/>
      </div>
   </div>
</template>

<style scoped>

</style>
