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
  text: i18n.t("cppListTip.text"),
  type: SCRIPT_UNITTEST,
  allowProportion: true,
  minSimilarPercent: 80,
  grade: 10,
  language:"cpp",
  correctAnswer:`
#include <vector>

std::vector<int> concat(const std::vector<int>& a, const std::vector<int>& b) {
    std::vector<int> result;
    result.reserve(a.size() + b.size());
    for (int val : a) {
        result.push_back(val);
    }
    for (int val : b) {
        result.push_back(val);
    }
    return result;
}
`,
  publicUnittests: [
    {
      inTest: "(std::vector<int>{1, 2, 3}), (std::vector<int>{4, 5, 6})",
      outTest: "(std::vector<int>{1, 2, 3, 4, 5, 6})",
      prefix: "public",
    }
  ],
  privateUnittests: [
    {
      inTest: "(std::vector<int>{1, 1, 1}), (std::vector<int>{2, 2, 2})",
      outTest: "(std::vector<int>{1, 1, 1, 2, 2, 2})",
      prefix: "private",
    }
  ],
  functionStructure:"std::vector<int> concat(const std::vector<int>& a, const std::vector<int>& b)",
  functionType: "sequence"
});
</script>

<template>
  <BaseTip
    :index="index"
    :item="item"
    :title="$t('cppListTip.title')"
    :description="$t('cppListTip.description').replace('#arr', '(std::vector<int>{1, 2, 3})')"
  ></BaseTip>
</template>

<style scoped></style>
