<script setup>
import FormWrapper from "@/components/FormWrapper.vue";
import { errorAlert } from "@/js/utility/utility.js";
import { MULTIPLE, SINGLE, SHORT, FULL, TYPES, SCRIPT, SCRIPT_UNITTEST } from "@/js/types.js";
import DotsMenu from "@/components/DotsMenu.vue";
import { copyObject, pasteObject } from "@/js/utility/clipboard.js";
import ChoiceProportion from "@/components/test/items/ChoiceProportion.vue";
import ChoiceAnswers from "@/components/test/items/ChoiceAnswers.vue";
import ShortAnswer from "@/components/test/items/ShortAnswer.vue";
import FullAnswer from "@/components/test/items/FullAnswer.vue";
import AnswerSimilarity from "@/components/test/items/AnswerSimilarity.vue";
import ScriptAnswer from "@/components/test/items/ScriptAnswer.vue";
import ScriptUnittestAnswer from "@/components/test/items/ScriptUnittestAnswer.vue";
import { formatItem } from "@/js/utility/item-formatter.js";
import { computed, nextTick, ref, watch } from "vue";

const props = defineProps({
  index: {
    type: Number,
    required: true,
  },
  testId: {
    type: String,
    required: true,
  },
  autoCheck: {
    type: Boolean,
    required: true,
  },
  onItemRemoved: {
    type: Function,
    required: true,
  },
  updateApi: {
    type: Function,
    required: true,
  },
  onItemPaste: {
    type: Function,
    required: true,
  },
  openPool: {
    type: Function,
    required: false,
    default: null,
  },
});

const formData = defineModel({ required: true });
const currentType = ref(formData.value.type);

const onUpdate = () => {
  formatItem(formData.value);
  props
    .updateApi(props.testId, props.index - 1, formData.value)
    .then((res) => {
      if (res.type !== currentType.value) formData.value = res;
      currentType.value = res.type;
    })
    .catch(errorAlert);
};

const onAddToPool = () => {
  props.openPool(formData.value, true);
};
const onPasteFromPool = () => {
  props.openPool(formData.value, false);
};

const onCopy = () => {
  copyObject("testItem", formData.value);
};
const onPaste = () => {
  const data = pasteObject("testItem");
  if (data) {
    formData.value = data;
  }
};

const onPasteNew = () => {
  const data = pasteObject("testItem");
  if (data) {
    props.onItemPaste(data);
  }
};

const textareaRef = ref(null);
const inputRef = ref(null);

const pressedEnter = computed(() => formData.value.text.includes("\n"));
const onPressed = () => {
  formData.value.text += "\n";

  nextTick(() => {
    textareaRef.value?.focus();
  });
};

watch(
  () => formData.value.text,
  () => {
    if (!formData.value.text.includes("\n")) {
      nextTick(() => {
        inputRef.value?.focus();
      });
    }
  },
);
</script>

<template>
  <FormWrapper class="mb-3">
    <form @change="onUpdate">
      <div>
        <div class="float-right">
          <DotsMenu>
            <div class="dropdown-item" @click="onItemRemoved">{{ $t("delete") }}</div>
            <div class="dropdown-item" @click="onCopy">{{ $t("copy") }}</div>
            <div class="dropdown-item" @click="onPaste">{{ $t("paste") }}</div>
            <div class="dropdown-item" @click="onPasteNew">{{ $t("pasteAsNew") }}</div>
            <div class="dropdown-item" @click="onPasteFromPool" v-if="openPool">
              {{ $t("pasteFromPool") }}
            </div>
            <div class="dropdown-item" @click="onAddToPool" v-if="openPool">
              {{ $t("addToPool") }}
            </div>
          </DotsMenu>
        </div>
        <label class="form-label" for="text">
          {{ index }}. <span class="wrap">{{ formData.text.trim() }}</span></label
        >
        <textarea
          ref="textareaRef"
          v-if="pressedEnter"
          v-model="formData.text"
          class="form-control"
          :placeholder="$t('questionText')"
          required
          maxlength="500"
          rows="4"
        ></textarea>
        <input
          ref="inputRef"
          v-else
          @keydown.enter="onPressed"
          v-model="formData.text"
          type="text"
          class="form-control"
          :placeholder="$t('questionText')"
          required
          maxlength="500"
        />
      </div>

      <div>
        <label class="form-label" for="type">{{ $t("type") }}</label>
        <select v-model="formData.type" class="form-select" required>
          <option v-for="(type, index) in TYPES" :value="type" :key="type" :selected="index === 0">
            {{ $t(type.toLowerCase()) }}
          </option>
        </select>
      </div>

      <div class="row mb-3">
        <ChoiceProportion
          v-if="[MULTIPLE, SCRIPT_UNITTEST].includes(formData.type) && autoCheck"
          v-model="formData"
        />

        <div class="col-md-6">
          <div class="input-group">
            <span class="input-group-text" id="basic-grade">{{ $t("grade") }}</span>
            <input
              v-model.trim="formData.grade"
              type="number"
              min="0"
              class="form-control mb-0"
              required
              aria-describedby="basic-grade"
            />
          </div>
        </div>
      </div>

      <ChoiceAnswers
        v-if="[SINGLE, MULTIPLE].includes(formData.type)"
        v-model="formData"
        :on-update="onUpdate"
      />

      <ShortAnswer v-if="[SHORT].includes(formData.type)" v-model="formData" />
      <FullAnswer v-else-if="[FULL].includes(formData.type)" v-model="formData" />
      <ScriptAnswer
        v-else-if="[SCRIPT].includes(formData.type)"
        v-model="formData"
        :on-update="onUpdate"
      />
      <ScriptUnittestAnswer
        v-else-if="[SCRIPT_UNITTEST].includes(formData.type)"
        v-model="formData"
        v-model:script="formData.correctAnswer"
        v-model:public-unittests="formData.publicUnittests"
        v-model:private-unittests="formData.privateUnittests"
        :on-update="onUpdate"
      />

      <AnswerSimilarity
        v-if="[SHORT, FULL, SCRIPT].includes(formData.type) && autoCheck"
        v-model="formData"
      />
    </form>
  </FormWrapper>
</template>

<style scoped>
button {
  margin: 0;
}

form {
  margin-bottom: 0;
}
.wrap {
  white-space: pre-wrap;
}
</style>
