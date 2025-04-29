<script setup>

const props = defineProps({
  onUpdate:{
    type: Function,
    required: true
  }
});

const formData = defineModel({required:true});

const allowUncheck = (item) => {
  if (formData.value.type !== "SINGLE" || !item.isCorrect) return true;

  const found = formData.value.choices.find((choice) => choice !== item && choice.isCorrect);

  return found !== undefined;
};

const addChoice = () => {
  formData.value.choices.push({ text: "", isCorrect: false });
  props.onUpdate();
};
</script>

<template>
  <div class="mb-3">
    <label class="form-label"
    >{{ $t("choices") }}
      <span class="btn btn-link" @click="addChoice"
      ><i class="fa-solid fa-plus"></i></span
      ></label>

    <div class="row" v-for="choice in formData.choices" :key="choice">
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

      <div class="col-8 col-md-9 col-lg-10">
        <input
          type="text"
          class="form-control"
          v-model.trim="choice.text"
          :placeholder="$t('choiceText')"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
