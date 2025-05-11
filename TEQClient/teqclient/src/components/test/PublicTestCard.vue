<script setup>
import { truncate } from "@/js/utility/utility.js";
import { CATEGORIES } from "@/js/categories.js";

defineProps({
  test: {
    type: Object,
    required: true,
  },
});

const getUrl = (category) => {
  return `/categories/${category}.png`;
};
</script>

<template>
  <div class="col-12 col-sm-6 col-md-4 col-lg-3 mt-3">
    <div class="card">
      <div class="card-header">
        <div>{{ test.title }}</div>
        <div class="badge bg-secondary" :title="$t('answerCount')">{{ test.answerCount }}</div>
      </div>
      <div class="card-body">
        <div class="badge bg-primary text-dark">{{ $t(test.category) }}</div>
        <img
          class="card-img"
          :src="getUrl(test.category ?? CATEGORIES[0])"
          :alt="$t('categoryType')"
        />
        <p v-if="test.description" class="mb-0">
          {{ truncate(test.description, 100) }}
        </p>
      </div>
      <div class="card-footer">
        <RouterLink :to="{ name: 'pass', params: { testId: test.id } }">{{
          $t("pass")
        }}</RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped>
.badge {
  position: absolute;
  top: 5px;
  right: 5px;
}
.card {
  height: 100%;
}
.card-img {
  width: 100%;
}
.card-body {
  position: relative;
}
</style>
