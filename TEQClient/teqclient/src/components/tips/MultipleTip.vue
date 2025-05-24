<script setup>
import { ref } from "vue";
import { MULTIPLE } from "@/js/types.js";
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
  text: i18n.t("multiTip.text"),
  type: MULTIPLE,
  allowProportion: true,
  grade: 4,
  choices: [
    { text: i18n.t("multiTip.choice1"), isCorrect: true },
    { text: i18n.t("multiTip.choice2"), isCorrect: false },
    { text: i18n.t("multiTip.choice3"), isCorrect: true },
    { text: i18n.t("multiTip.choice4"), isCorrect: false },
  ],
});
</script>

<template>
  <BaseTip
    :index="index"
    :item="item"
    :title="$t('multiTip.title')"
    :description="$t('multiTip.description')"
  ></BaseTip>
</template>

<style scoped></style>
