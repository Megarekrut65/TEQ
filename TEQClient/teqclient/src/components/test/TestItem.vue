<script setup>
import FormWrapper from "@/components/FormWrapper.vue";
import { itemUpdateApi } from "@/js/api/item.js";
import { errorAlert } from "@/js/utility/utility.js";
import { MULTIPLE, SINGLE, TEXT } from "@/js/types.js";
import { defaultChoices } from "@/js/data-types.js";

const props = defineProps({
  index:{
    type: Number,
    required: true
  },
  testId:{
    type: String,
    required: true
  },
  autoCheck:{
    type: Boolean,
    required: true
  },
  onItemRemoved:{
    type: Function,
    required: true
  }
});

const formData = defineModel({required:true});

const allowUncheck = (item)=>{
  if(formData.value.type !== "SINGLE" || !item.isCorrect) return true;

  const found =  formData.value.choices.find(choice=>choice !== item && choice.isCorrect);

  return found !== undefined;
};

const onUpdate = ()=>{
  if(formData.value.type === SINGLE || formData.value.type === MULTIPLE
    && (formData.value.choices == null || formData.value.choices.length === 0)){
    formData.value.choices = defaultChoices();
  }

  itemUpdateApi(props.testId, props.index-1, formData.value).catch(errorAlert);
};

const addChoice = () => {
  formData.value.choices.push({ text: "", isCorrect: false });
  onUpdate();
};


</script>

<template>
  <FormWrapper class="mb-3">
    <form  @change="onUpdate">
      <div>
        <div class="btn-trash" @click="onItemRemoved"><i class="fa-solid fa-trash-can"></i></div>
        <label class="form-label" for="text">{{index}}. {{ formData.text }}</label>
        <input
          v-model.trim="formData.text"
          type="text"
          class="form-control"
          :placeholder="$t('questionText')"
          required
        />
      </div>

      <div>
        <label class="form-label" for="type">{{ $t("type") }}</label>
        <select v-model="formData.type" class="form-select" required >
          <option value="SINGLE">{{ $t("singleChoice") }}</option>
          <option value="MULTIPLE">{{ $t("multipleChoice") }}</option>
          <option value="TEXT">{{ $t("textAnswer") }}</option>
        </select>
      </div>

      <div class="row mb-3">
        <div class="col-md-6" v-if="formData.type !== SINGLE && autoCheck">
          <div class="form-check form-switch">
            <input class="form-check-input" type="checkbox" role="switch"
                   v-model="formData.allowProportion">
            <label class="form-check-label" :title="$t('allowProportionHint')">{{$t('allowProportion')}}</label>
          </div>
        </div>
        <div class="col-md-6">
          <div class="input-group">
            <span class="input-group-text" id="basic-grade">{{$t('grade')}}</span>
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

      <div v-if="formData.type === SINGLE || formData.type === MULTIPLE" class="mb-3">
        <label class="form-label">{{ $t("choices") }} <span class="btn btn-link" @click="addChoice"><i class="fa-solid fa-plus"></i></span></label>

        <div class="row" v-for="choice in formData.choices" :key="choice">
          <div class="col-4 col-md-3 col-lg-2">
            <div class="form-check form-switch">
              <input class="form-check-input" type="checkbox" role="switch"
                     v-model="choice.isCorrect" :disabled="!allowUncheck(choice)">
              <label class="form-check-label" >{{$t('correct')}}</label>
            </div>
          </div>

          <div class="col-8 col-md-9 col-lg-10">
            <input type="text" class="form-control" v-model.trim="choice.text" :placeholder="$t('choiceText')" >
          </div>

        </div>


      </div>

      <div v-if="formData.type === TEXT" class="mb-3">
        <label for="correctAnswer" class="form-label">{{ $t("correctAnswer") }}</label>
        <textarea
          v-model="formData.correctAnswer"
          class="form-control"
          rows="3"
        ></textarea>
      </div>
      <div v-if="formData.type === TEXT" class="mb-3">
        <label class="form-label" for="text" :title="$t('minSimilarHnt')">{{$t('minSimilar')}}</label>
        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-percent">%</span>
          <input
            v-model.number="formData.minSimilarPercent"
            type="number"
            min="0"
            max="100"
            class="form-control mb-0"
            required
            aria-describedby="basic-percent"
          />
        </div>

      </div>

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
</style>
