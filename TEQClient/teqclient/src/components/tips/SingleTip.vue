<script setup>
import { ref } from "vue";
import { SINGLE } from "@/js/types.js";
import BaseTip from "@/components/tips/BaseTip.vue";
import i18n from "@/i18n/index.js";

defineProps({
  index: {
    type: Number,
    required: true,
  },
});

i18n.useT();

const item = ref({
  text: i18n.t("singleTip.text"),
  type: SINGLE,
  allowProportion: false,
  grade: 1,
  choices: [
    { text: i18n.t("singleTip.choice1"), isCorrect: false },
    { text: i18n.t("singleTip.choice2"), isCorrect: true },
    { text: i18n.t("singleTip.choice3"), isCorrect: false },
  ],
});
</script>

<template>
  <BaseTip
    :index="index"
    :item="item"
    :title="$t('singleTip.title')"
    :description="$t('singleTip.description')"
  ></BaseTip>
</template>

<style scoped></style>
