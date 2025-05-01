<script setup>
import { ref, watch } from "vue";
import { getLanguage } from "@/js/languages.js";
import UnittestItem from "@/components/test/items/UnittestItem.vue";
import { defaultUnitTest } from "@/js/data-types.js";
import { RETURN_TYPES } from "@/js/types.js";
import ScriptEditorTest from "@/components/script/ScriptEditorTest.vue";

const props = defineProps({
  onUpdate: {
    type: Function,
    required: true,
  },
});

const formData = defineModel({ required: true });
const language = ref(getLanguage(formData.value.language));

watch(language, () => {
  if (formData.value.language === language.value?.type) return;

  formData.value.language = language.value?.type;
});

const publicOn = ref(true);

const addTest = () => {
  const container = publicOn.value
    ? formData.value.publicUnittests
    : formData.value.privateUnittests;

  const prefix = publicOn.value ? "public" : "private";

  container.push(defaultUnitTest(prefix));
  props.onUpdate();
};

const onUnitRemoved = (index) => {
  const container = publicOn.value
    ? formData.value.publicUnittests
    : formData.value.privateUnittests;

  if (index < 0 || index >= container.length) return;

  container.splice(index, 1);
  props.onUpdate();
};

const testData = () => {
  const unittests = publicOn.value
    ? formData.value.publicUnittests
    : formData.value.privateUnittests;

  return {
    functionStructure: formData.value.functionStructure,
    functionType: formData.value.functionType,
    unittests,
  };
};
</script>

<template>
  <div class="mb-3 row unit-item">
    <div class="col-12 col-md-6">
      <label for="correctAnswer" class="form-label">{{ $t("tryTesting") }}</label>
      <ScriptEditorTest
        v-model:language="language"
        v-model:script="formData.correctAnswer"
        :key="formData.type"
        :on-changed="onUpdate"
        :test-data="testData()"
      >
      </ScriptEditorTest>
    </div>
    <div class="col-12 col-md-6">
      <div class="mb-3">
        <label class="form-label">{{ $t("testFunStruct") }}</label>
        <input
          type="text"
          class="form-control"
          :placeholder="language?.testFunStruct"
          v-model="formData.functionStructure"
        />
      </div>
      <div class="input-group mb-3">
        <label class="input-group-text mb-0">{{ $t("returnType") }}</label>
        <select class="form-select mb-0" v-model="formData.functionType">
          <option v-for="type in RETURN_TYPES" :key="type" :value="type">{{ type }}</option>
        </select>
      </div>
      <ul class="nav nav-tabs">
        <li class="nav-item">
          <div
            :class="{ 'nav-link btn-hover': true, active: publicOn }"
            aria-current="page"
            :title="$t('publicUnitHint')"
            @click="publicOn = !publicOn"
          >
            {{ $t("publicUnit") }}
          </div>
        </li>
        <li class="nav-item">
          <div
            :class="{ 'nav-link btn-hover': true, active: !publicOn }"
            :title="$t('privateUnitHint')"
            @click="publicOn = !publicOn"
          >
            {{ $t("privateUnit") }}
          </div>
        </li>
      </ul>

      <div v-if="publicOn" class="unittests">
        <div class="mb-1 btn-hover" @click="addTest"><i class="fa-solid fa-plus"></i></div>
        <UnittestItem
          v-for="(item, index) in formData.publicUnittests"
          :key="item"
          v-model="formData.publicUnittests[index]"
          :index="index"
          :count="formData.publicUnittests.length"
          :on-removed="() => onUnitRemoved(item)"
        />
      </div>
      <div v-else class="unittests">
        <div class="mb-1 btn-hover" @click="addTest"><i class="fa-solid fa-plus"></i></div>
        <UnittestItem
          v-for="(item, index) in formData.privateUnittests"
          :key="item"
          v-model="formData.privateUnittests[index]"
          :index="index"
          :count="formData.privateUnittests.length"
          :on-removed="() => onUnitRemoved(item)"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.unittests {
  max-height: 80vh;
  overflow-y: auto;
}
</style>
