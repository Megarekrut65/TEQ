<script setup>
import { ref } from "vue";
import { SHORT } from "@/js/types.js";
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
  text: i18n.t("shortTip.text"),
  type: SHORT,
  allowProportion: false,
  minSimilarPercent: 90,
  grade: 5,
  correctAnswer:i18n.t("shortTip.answer")
});
</script>

<template>
  <BaseTip
    :index="index"
    :item="item"
    :title="$t('shortTip.title')"
    :description="$t('shortTip.description')"
  ></BaseTip>
</template>

<style scoped></style>
