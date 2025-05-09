<script setup>
import { FULL, MULTIPLE, SCRIPT, SCRIPT_UNITTEST, SHORT, SINGLE } from "@/js/types.js";
import { answerItemUpdateApi } from "@/js/api/answer.js";
import { errorAlert } from "@/js/utility/utility.js";
import PassChoiceAnswers from "@/components/pass/pass-items/PassChoiceAnswers.vue";
import PassTextItem from "@/components/pass/pass-items/PassTextItem.vue";
import PassScriptUnittestItem from "@/components/pass/pass-items/PassScriptUnittestItem.vue";

const props = defineProps({
  answerId: {
    type: String,
    required: true,
  },
  index: {
    type: Number,
    required: true,
  },
  readonly: {
    type: Boolean,
    required: false,
    default: false,
  },
  showCorrect: {
    type: Boolean,
    required: false,
    default: false,
  },
  autoCheck: {
    type: Boolean,
    required: false,
    default: false,
  },
  item: {
    type: Object,
    required: true,
  },
  isOwner: {
    type: Boolean,
    required: false,
    default: false,
  },
  updateGrade: {
    type: Function,
    required: true,
  },
});

const formData = defineModel({ required: true });

const updateGrade = () => {
  answerItemUpdateApi(props.answerId, props.index - 1, formData.value)
    .then(() => props.updateGrade())
    .catch(errorAlert);
};
</script>

<template>
  <div class="card mt-3">
    <div class="card-body">
      <div class="d-flex justify-content-between">
        <label>{{ index }}. {{ item.text }}</label>
        <div v-if="isOwner" class="badge">
          <label class="form-label text-dark"
            >{{ $t("grade") }}({{ formData.grade }}/{{ item.grade }})</label
          >
          <input
            @change="updateGrade"
            class="form-control"
            type="number"
            v-model="formData.grade"
          />
        </div>
        <div v-else-if="showCorrect" class="badge bg-secondary">
          {{ formData.grade }}/{{ item.grade }}
        </div>
      </div>

      <PassChoiceAnswers
        v-if="[SINGLE, MULTIPLE].includes(item.type)"
        :show-correct="showCorrect"
        :readonly="readonly"
        v-model="formData"
        :item="item"
        :index="index"
      />
      <PassTextItem
        v-else-if="[FULL, SHORT, SCRIPT].includes(item.type)"
        :show-correct="showCorrect"
        :auto-check="autoCheck"
        :readonly="readonly"
        v-model="formData"
        :item="item"
        :index="index"
      />
      <PassScriptUnittestItem
        v-else-if="[SCRIPT_UNITTEST].includes(item.type)"
        :show-correct="showCorrect"
        :readonly="readonly"
        v-model="formData"
        :item="item"
      />
    </div>
  </div>
</template>

<style scoped>
button {
  margin: 0;
}

form {
  margin-bottom: 0;
}

.badge {
  height: min-content;
}
</style>
