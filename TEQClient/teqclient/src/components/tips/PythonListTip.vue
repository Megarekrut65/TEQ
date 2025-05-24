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
  text: i18n.t("pythonListTip.text"),
  type: SCRIPT_UNITTEST,
  allowProportion: true,
  minSimilarPercent: 80,
  grade: 10,
  language:"python",
  correctAnswer:`
def concat(lst1, lst2):
    return lst1 + lst2
`,
  publicUnittests: [
    {
      inTest: "[1, 2, 3], [4, 5, 6]",
      outTest: "[1, 2, 3, 4, 5, 6]",
      prefix: "public",
    }
  ],
  privateUnittests: [
    {
      inTest: "[1, 1, 1], [2, 2, 2]",
      outTest: "[1, 1, 1, 2, 2, 2]",
      prefix: "private",
    }
  ],
  functionStructure:"def concat(lst1, lst2)",
  functionType: "sequence"
});
</script>

<template>
  <BaseTip
    :index="index"
    :item="item"
    :title="$t('pythonListTip.title')"
    :description="$t('pythonListTip.description')"
  ></BaseTip>
</template>

<style scoped></style>
