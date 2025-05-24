<script setup>
import { ref, watch } from "vue";
import { getLanguage, isDefaultStructure, languages } from "@/js/languages.js";
import UnittestItem from "@/components/test/items/UnittestItem.vue";
import { defaultUnitTest, defaultUnitTests } from "@/js/data-types.js";
import { RETURN_TYPES } from "@/js/types.js";
import ScriptEditorTest from "@/components/script/ScriptEditorTest.vue";

const props = defineProps({
  onUpdate: {
    type: Function,
    required: false,
    default: () => {},
  },
});

const expand = ref(false);

const formData = defineModel({
  required: false,
  default: {
    language: languages[0].type,
    functionType: RETURN_TYPES[0],
    functionStructure: languages[0].testFunStruct,
  },
});

const script = defineModel("script", { required: false, default: languages[0].testFun });
const publicUnittests = defineModel("publicUnittests", {
  required: false,
  default: () => defaultUnitTests("public"),
});
const privateUnittests = defineModel("privateUnittests", {
  required: false,
  default: () => defaultUnitTests("private"),
});

const language = ref(getLanguage(formData.value.language));

watch(language, () => {
  if (formData.value.language === language.value?.type) return;

  formData.value.language = language.value?.type;
  if (isDefaultStructure(formData.value.functionStructure)) {
    formData.value.functionStructure = language.value?.testFunStruct;
  }
});

const publicOn = ref(true);

const addTest = () => {
  const container = publicOn.value ? publicUnittests.value : privateUnittests.value;

  const prefix = publicOn.value ? "public" : "private";

  container.push(defaultUnitTest(prefix));
  props.onUpdate();
};

const onUnitRemoved = (index) => {
  const container = publicOn.value ? publicUnittests.value : privateUnittests.value;

  if (index < 0 || index >= container.length) return;

  container.splice(index, 1);
  props.onUpdate();
};

const testData = () => {
  const unittests = publicOn.value ? publicUnittests.value : privateUnittests.value;

  return {
    functionStructure: formData.value.functionStructure,
    functionType: formData.value.functionType,
    unittests,
  };
};
</script>

<template>
  <div class="mb-3 row unit-item" >
    <div :class="{'col-12':true, 'col-md-6':!expand, 'mb-3':expand}">
      <label for="correctAnswer" class="form-label">{{ $t("tryTesting") }}
        <i :class="{'fa-solid btn-hover':true, 'fa-maximize':!expand, 'fa-minimize':expand }" @click="expand=!expand"></i></label>
      <ScriptEditorTest
        v-model:language="language"
        v-model:script="script"
        :key="formData.type"
        :on-changed="onUpdate"
        :test-data="testData()"
      >
      </ScriptEditorTest>
    </div>
    <div :class="{'col-12':true, 'col-md-6':!expand}">
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
          v-for="(item, index) in publicUnittests"
          :key="item"
          v-model="publicUnittests[index]"
          :index="index"
          :count="publicUnittests.length"
          :on-removed="() => onUnitRemoved(index)"
        />
      </div>
      <div v-else class="unittests">
        <div class="mb-1 btn-hover" @click="addTest"><i class="fa-solid fa-plus"></i></div>
        <UnittestItem
          v-for="(item, index) in privateUnittests"
          :key="item"
          v-model="privateUnittests[index]"
          :index="index"
          :count="privateUnittests.length"
          :on-removed="() => onUnitRemoved(index)"
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
