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
  text: i18n.t("javaListTip.text"),
  type: SCRIPT_UNITTEST,
  allowProportion: true,
  minSimilarPercent: 80,
  grade: 10,
  language: "java",
  correctAnswer: `
class Solution {
    public static java.util.List<java.lang.Integer> concat(java.util.List<java.lang.Integer> a, java.util.List<java.lang.Integer> b) {
        java.util.List<java.lang.Integer> result = new java.util.ArrayList<>(a.size() + b.size());
        for (java.lang.Integer val : a) {
            result.add(val);
        }
        for (java.lang.Integer val : b) {
            result.add(val);
        }
        return result;
    }
}
  `,
  publicUnittests: [
    {
      inTest: "java.util.Arrays.asList(1, 2, 3), java.util.Arrays.asList(4, 5, 6)",
      outTest: "java.util.Arrays.asList(1, 2, 3, 4, 5, 6)",
      prefix: "public",
    }
  ],
  privateUnittests: [
    {
      inTest: "java.util.Arrays.asList(1, 1, 1), java.util.Arrays.asList(2, 2, 2)",
      outTest: "java.util.Arrays.asList(1, 1, 1, 2, 2, 2)",
      prefix: "private",
    }
  ],
  functionStructure: "java.util.List<Integer> concat(java.util.List<Integer> a, java.util.List<Integer> b)",
  functionType: "sequence"
});

</script>

<template>
  <BaseTip
    :index="index"
    :item="item"
    :title="$t('javaListTip.title')"
    :description="$t('javaListTip.description')"
  ></BaseTip>
</template>

<style scoped></style>
