<script setup>
import { ref } from "vue";
import { errorAlert } from "@/js/utility/utility.js";

const props = defineProps({
  type: {
    type: String,
    required: true,
  },
  runFunction: {
    type: Function,
    required: true,
  },
});

const text1 = ref("");
const text2 = ref("");
const similarity = ref("- ");

const isRunning = ref(false);

const run = () => {
  isRunning.value = true;
  similarity.value = "- ";

  props
    .runFunction(text1.value, text2.value)
    .then((res) => {
      similarity.value = (res * 100).toFixed(2);
    })
    .catch(errorAlert)
    .finally(() => {
      isRunning.value = false;
    });
};
</script>

<template>
  <div class="row">
    <div class="col-12 col-md-6">
      <button
        class="btn btn-outline-secondary"
        :disabled="isRunning || text1.length === 0 || text2.length === 0"
        @click="run"
      >
        {{ $t("check") }}
      </button>
    </div>
    <div class="col-12 col-md-6 d-flex align-items-center">
      <span
        :class="{ 'badge text-dark': true, 'bg-primary': isRunning, 'bg-secondary': !isRunning }"
        >{{ $t("similarity") }} {{ similarity }}%</span
      >
    </div>

    <div class="col-12 col-md-6 mt-2">
      <label for="correctAnswer" class="form-label">{{ $t("first" + type) }}</label>
      <textarea v-model.trim="text1" class="form-control" rows="3" maxlength="5000"></textarea>
    </div>
    <div class="col-12 col-md-6 mt-2">
      <label for="correctAnswer" class="form-label">{{ $t("second" + type) }}</label>
      <textarea v-model.trim="text2" class="form-control" rows="3" maxlength="5000"></textarea>
    </div>
  </div>
</template>

<style scoped></style>
