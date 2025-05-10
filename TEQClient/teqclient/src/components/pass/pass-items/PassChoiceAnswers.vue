<script setup>
import { SINGLE } from "@/js/types.js";

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
  <div class="mb-3">
    <label class="form-label">{{ $t("choices") }}</label>

    <div v-for="(choice, i) in item.choices" :key="choice">
      <div class="form-check">
        <input
          v-if="[SINGLE].includes(item.type)"
          class="form-check-input"
          type="radio"
          :name="`radio_${index}`"
          v-model="formData.choices[0]"
          :value="i"
          :disabled="readonly"
        />

        <input
          v-else
          class="form-check-input"
          type="checkbox"
          v-model="formData.choices"
          :value="i"
          :disabled="readonly"
        />

        <label
          :class="{
            'form-check-label': true,
            'text-success': showCorrect && choice.isCorrect,
          }"
        >
          {{ choice.text }}<i v-if="showCorrect && choice.isCorrect" class="fa-solid fa-check"></i>
        </label>
      </div>
    </div>
    <input
      class="hide"
      type="radio"
      :name="`radio_${index}`"
      v-model="formData.choices[0]"
      value="-1"
    />
  </div>
</template>

<style scoped>
.hide {
  display: none;
}
</style>
