<script setup>
import { FULL, SCRIPT, SHORT } from "@/js/types.js";
import PassFulItem from "@/components/pass/pass-items/PassFullItem.vue";
import PassScriptItem from "@/components/pass/pass-items/PassScriptItem.vue";

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
  autoCheck: {
    type: Boolean,
    required: true,
  },
});

const formData = defineModel({ required: true });
</script>

<template>
  <div class="mb-3">
    <div v-if="showCorrect && autoCheck" class="badge text-dark bg-warning sim-badge">
      {{ formData.similarity.toFixed(1) }}%
    </div>

    <PassFulItem v-if="[FULL].includes(item.type)" v-model="formData" :readonly="readonly" />

    <input
      v-else-if="[SHORT].includes(item.type)"
      v-model="formData.answer"
      class="form-control"
      type="text"
      :readonly="readonly"
    />

    <PassScriptItem
      v-else-if="[SCRIPT].includes(item.type)"
      :item="item"
      :readonly="readonly"
      v-model="formData"
    />

    <div v-if="showCorrect && item.correctAnswer">
      <span class="text-success">{{ $t("answer") }}</span>
      <p>{{ item.correctAnswer }}</p>
    </div>
  </div>
</template>

<style scoped></style>
