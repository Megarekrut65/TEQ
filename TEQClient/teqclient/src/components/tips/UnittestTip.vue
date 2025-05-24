<script setup>
import { ref } from "vue";
import { SCRIPT_UNITTEST } from "@/js/types.js";
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
  text: i18n.t("unittestTip.text"),
  type: SCRIPT_UNITTEST,
  allowProportion: true,
  minSimilarPercent: 80,
  grade: 15,
  language:"python",
  correctAnswer:`
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
`,
  publicUnittests: [
    {
      inTest: "5",
      outTest: "120",
      prefix: "public",
    },
    {
      inTest: "0",
      outTest: "1",
      prefix: "public",
    },
  ],
  privateUnittests: [
    {
      inTest: "1",
      outTest: "1",
      prefix: "private",
    },
    {
      inTest: "6",
      outTest: "720",
      prefix: "private",
    },
  ],
  functionStructure:"def factorial(n)",
  functionType: "integer"
});
</script>

<template>
  <BaseTip
    :index="index"
    :item="item"
    :title="$t('unittestTip.title')"
    :description="$t('unittestTip.description')"
  ></BaseTip>
</template>

<style scoped></style>
