<script setup>
const props = defineProps({
  onUpdate: {
    type: Function,
    required: true,
  },
});

const formData = defineModel({ required: true });

const allowUncheck = (item) => {
  if (formData.value.type !== "SINGLE" || !item.isCorrect) return true;

  const found = formData.value.choices.find((choice) => choice !== item && choice.isCorrect);

  return found !== undefined;
};

const allowRemove = (item) => {
  if (formData.value.choices.length <= 1) return false;

  if (formData.value.type !== "SINGLE" || !item.isCorrect) return true;

  const found = formData.value.choices.find((choice) => choice !== item && choice.isCorrect);

  return found !== undefined;
};

const addChoice = () => {
  formData.value.choices.push({ text: "", isCorrect: false });
  props.onUpdate();
};

const onChoiceRemoved = (index) => {
  if (index < 0 || index >= formData.value.choices.length) return;

  formData.value.choices.splice(index, 1);
  props.onUpdate();
};
</script>

<template>
  <div class="mb-3">
    <label class="form-label"
      >{{ $t("choices") }}
      <span class="btn btn-link" @click="addChoice" v-if="formData.choices?.length < 10"
        ><i class="fa-solid fa-plus"></i></span
    ></label>

    <div class="row" v-for="(choice, i) in formData.choices" :key="choice">
      <div class="col-4 col-md-3 col-lg-2">
        <div class="form-check form-switch">
          <input
            class="form-check-input"
            type="checkbox"
            role="switch"
            v-model="choice.isCorrect"
            :disabled="!allowUncheck(choice)"
          />
          <label class="form-check-label">{{ $t("correct") }}</label>
        </div>
      </div>

      <div class="col-8 col-md-9 col-lg-10 d-flex justify-content-between">
        <input
          type="text"
          class="form-control"
          v-model.trim="choice.text"
          maxlength="200"
          :placeholder="$t('choiceText')"
        />
        <div class="btn-hover ms-3" @click="() => onChoiceRemoved(i)" v-if="allowRemove(choice)">
          <i class="fa-solid fa-trash-can"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
