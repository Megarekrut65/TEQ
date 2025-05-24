<script setup>
import { ref } from "vue";
import { FULL } from "@/js/types.js";
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
  text: i18n.t("fullTip.text"),
  type: FULL,
  allowProportion: false,
  minSimilarPercent: 80,
  grade: 10,
  correctAnswer:i18n.t("fullTip.answer")
});
</script>

<template>
  <BaseTip
    :index="index"
    :item="item"
    :title="$t('fullTip.title')"
    :description="$t('fullTip.description')"
  ></BaseTip>
</template>

<style scoped></style>
