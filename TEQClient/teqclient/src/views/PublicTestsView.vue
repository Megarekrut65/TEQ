<script setup>
import { ref, watch } from "vue";
import { publicTestListApi } from "@/js/api/test.js";
import { errorAlert } from "@/js/utility/utility.js";
import PublicTestCard from "@/components/test/PublicTestCard.vue";
import { useRoute } from "vue-router";
import { CATEGORIES } from "@/js/categories.js";

const tests = ref([]);

const route = useRoute();

const updatePage = () => {
  publicTestListApi(route.query.category)
    .then((res) => {
      tests.value = res.results;
    })
    .catch(errorAlert);
};

watch(() => route.query.category, updatePage);

updatePage();
</script>

<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-6 col-md-4 col-lg-3">
        <RouterLink :to="{ name: 'public' }" :class="{ active: !route.query.category }"
          >{{ $t("all") }} <i class="fa-solid fa-eye"></i
        ></RouterLink>
      </div>
      <div v-for="cat in CATEGORIES" :key="cat" class="col-6 col-md-4 col-lg-3">
        <RouterLink
          :to="{ name: 'public', query: { category: cat } }"
          :class="{ active: cat === route.query.category }"
          >{{ $t(cat) }} <i class="fa-solid fa-eye"></i
        ></RouterLink>
      </div>
    </div>

    <div class="row mt-4">
      <PublicTestCard v-for="test in tests" :key="test.id" :test="test" />
    </div>
  </div>
</template>

<style scoped>
.active {
  color: rgb(242, 137, 63);
}
</style>
