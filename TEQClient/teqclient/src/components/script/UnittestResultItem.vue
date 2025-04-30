<script setup>
defineProps({
  testName: {
    type: String,
    required: true,
  },
  failure: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <div>
    <details v-if="failure">
      <summary class="text-danger">
        <strong>{{ testName }} <i class="fa-solid fa-xmark"></i></strong>
      </summary>
      <div v-if="failure">{{ failure.reason }}</div>
    </details>
    <div v-else class="text-success">
      <strong>{{ testName }} <i class="fa-solid fa-check"></i></strong>
    </div>
  </div>
</template>

<style scoped></style>
