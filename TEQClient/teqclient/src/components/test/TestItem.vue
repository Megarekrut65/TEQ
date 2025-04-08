<script setup>
import FormWrapper from "@/components/FormWrapper.vue";
import { itemUpdateApi } from "@/js/api/item.js";
import { errorAlert } from "@/js/utility/utility.js";  // Example API calls for create/update

const props = defineProps({
  index:{
    type: Number,
    required: true
  },
  testId:{
    type: String,
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
  console.log(found);

  return found !== undefined;
};

const onUpdate = ()=>{
  itemUpdateApi(props.testId, props.index-1, formData.value).catch(errorAlert);
};

const addChoice = () => {
  formData.value.choices.push({ text: "", isCorrect: false });
  onUpdate();
};


</script>

<template>
  <FormWrapper class="mb-3">
    <form>
      <div>
        <div class="btn-trash" @click="onItemRemoved"><i class="fa-solid fa-trash-can"></i></div>
        <label class="form-label" for="text">{{index}}. {{ formData.text }}</label>
        <input
          v-model.trim="formData.text"
          type="text"
          class="form-control"
          :placeholder="$t('questionText')"
          @change="onUpdate"
          required
        />
      </div>

      <div>
        <label class="form-label" for="type">{{ $t("type") }}</label>
        <select v-model="formData.type" class="form-select" required @change="onUpdate">
          <option value="SINGLE">{{ $t("singleChoice") }}</option>
          <option value="MULTIPLE">{{ $t("multipleChoice") }}</option>
          <option value="TEXT">{{ $t("textAnswer") }}</option>
        </select>
      </div>

      <div v-if="formData.type === 'SINGLE' || formData.type === 'MULTIPLE'" class="mb-3">
        <label class="form-label">{{ $t("choices") }} <span class="btn btn-link" @click="addChoice"><i class="fa-solid fa-plus"></i></span></label>

        <div class="row" v-for="choice in formData.choices" :key="choice">
          <div class="col-4 col-md-3 col-lg-2">
            <div class="form-check form-switch">
              <input class="form-check-input" type="checkbox" role="switch"
                     v-model="choice.isCorrect" @change="onUpdate" :disabled="!allowUncheck(choice)">
              <label class="form-check-label" >{{$t('correct')}}</label>
            </div>
          </div>

          <div class="col-8 col-md-9 col-lg-10">
            <input type="text" class="form-control" v-model.trim="choice.text" :placeholder="$t('choiceText')" @change="onUpdate">
          </div>

        </div>


      </div>

      <div v-if="formData.type === 'TEXT'" class="mb-3">
        <label for="correctAnswer" class="form-label">{{ $t("correctAnswer") }}</label>
        <textarea
          v-model="formData.correctAnswer"
          class="form-control"
          rows="3"
        ></textarea>
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
