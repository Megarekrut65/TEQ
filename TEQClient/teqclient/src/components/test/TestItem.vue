<script setup>
import { ref } from "vue";
import LoadingWindow from "@/components/LoadingWindow.vue";
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
  instance: {
    type: Object,
    required: true
  }
});

const formData = ref(props.instance);
const loading = ref(false);

const onUpdate = ()=>{
  itemUpdateApi(props.testId, props.index-1, formData.value).then(res=>{
    console.log(res);
  }).catch(errorAlert);
};

const addChoice = () => {
  formData.value.choices.push({ text: "", isCorrect: false });
  onUpdate();
};


</script>

<template>
  <LoadingWindow v-if="loading" />
  <FormWrapper class="mb-3">
    <form @submit.prevent="onSubmit">
      <div>
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
              <input class="form-check-input" type="checkbox" role="switch" id="switchCheckDefault"
                     v-model="choice.isCorrect" @change="onUpdate">
              <label class="form-check-label" for="switchCheckDefault">{{$t('correct')}}</label>
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
