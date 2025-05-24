<script setup>
import { ref } from "vue";
import { SCRIPT } from "@/js/types.js";
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
  text: i18n.t("scriptTip.text"),
  type: SCRIPT,
  allowProportion: false,
  minSimilarPercent: 80,
  grade: 10,
  language:"cpp",
  correctAnswer:`#include <iostream>
#include <vector>
#include <algorithm>

void bubbleSort(std::vector<int>& arr) {
	for (size_t i = 0; i < arr.size(); ++i)
		for (size_t j = 0; j < arr.size() - i - 1; ++j)
			if (arr[j] > arr[j + 1]) std::swap(arr[j], arr[j + 1]);
}

int main() {
	std::vector<int> data = {5, 3, 8, 4, 2};
	bubbleSort(data);
	for (int x : data) std::cout << x << " ";
	std::cout << std::endl;
	return 0;
}
`
});
</script>

<template>
  <BaseTip
    :index="index"
    :item="item"
    :title="$t('scriptTip.title')"
    :description="$t('scriptTip.description')"
  ></BaseTip>
</template>

<style scoped></style>
