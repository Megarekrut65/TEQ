<script setup>
import { FULL, SCRIPT, SHORT } from "@/js/types.js";
import PassFulItem from "@/components/pass/pass_items/PassFulItem.vue";

defineProps({
  index: {
    type: Number,
    required: true,
  },
  item: {
    type: Object,
    required: true,
  },
  readonly: {
    type: Boolean,
    required: true,
  },
  showCorrect: {
    type: Boolean,
    required: true,
  },
});

const formData = defineModel({ required: true });
</script>

<template>
  <div v-if="[FULL, SHORT, SCRIPT].includes(formData.type)" class="mb-3">
    <div v-if="showCorrect && autoCheck" class="badge text-dark bg-warning sim-badge">
      {{ formData.similarity.toFixed(1) }}%
    </div>

    <PassFulItem v-if="[FULL].includes(formData.type)" v-model="formData" :readonly="readonly" />

    <input v-else v-model="formData.answer" class="form-control" type="text" :readonly="readonly" />

    <div v-if="showCorrect && item.correctAnswer">
      <span class="text-success">{{ $t("answer") }}</span>
      <p>{{ item.correctAnswer }}</p>
    </div>
  </div>
</template>

<style scoped></style>
