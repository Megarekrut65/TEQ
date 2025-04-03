<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import LoadingWindow from "@/components/LoadingWindow.vue";
import { errorAlert } from "@/js/utility/utility.js";
import { itemCreateApi } from "@/js/api/item.js";
import FormWrapper from "@/components/FormWrapper.vue";  // Example API calls for create/update

const props = defineProps({
  instance: {
    type: Object,
    required: false,
    default: () => {
      return {
        testId: "",
        text: "",
        type: "SINGLE",  // Default type to 'SINGLE'
        choices: [{ text: "", is_correct: false }],
        correctAnswer: "",
      };
    },
  },
  mode: {
    type: String,
    required: false,
    default: "create",
  },
});

const formData = ref(props.instance);
const loading = ref(false);
const router = useRouter();

const createItem = () => {
  return itemCreateApi(formData.value).then((res) => {
    router.push({ name: "itemEditor", params: { itemId: res.id } });
  });
};

const updateItem = () => {
  return itemCreateApi(props.instance.id, formData.value).then((res) => {
    formData.value = res;
  });
};

const api = props.mode === "create" ? createItem : updateItem;

const onSubmit = () => {
  loading.value = true;

  api().catch(errorAlert).finally(() => {
    loading.value = false;
  });
};

const addChoice = () => {
  formData.value.choices.push({ text: "", is_correct: false });
};

</script>

<template>
  <LoadingWindow v-if="loading" />
  <FormWrapper :title="$t(mode) + ' ' + $t('item')">
    <form @submit.prevent="onSubmit">
      <div>
        <label class="form-label" for="testId">{{ $t("testId") }}</label>
        <input
          v-model.trim="formData.testId"
          type="text"
          class="form-control"
          required
        />
      </div>

      <div>
        <label class="form-label" for="text">{{ $t("text") }}</label>
        <input
          v-model.trim="formData.text"
          type="text"
          class="form-control"
          required
        />
      </div>

      <div>
        <label class="form-label" for="type">{{ $t("type") }}</label>
        <select v-model="formData.type" class="form-select" required>
          <option value="SINGLE">{{ $t("singleChoice") }}</option>
          <option value="MULTIPLE">{{ $t("multipleChoice") }}</option>
          <option value="TEXT">{{ $t("textAnswer") }}</option>
        </select>
      </div>

      <!-- Choices Field (for Single and Multiple types) -->
      <div v-if="formData.type === 'SINGLE' || formData.type === 'MULTIPLE'" class="mb-3">
        <label class="form-label">{{ $t("choices") }}</label>
        <div
          v-for="(choice, index) in formData.choices"
          :key="index"
          class="input-group mb-2"
        >
          <input
            v-model="choice.text"
            type="text"
            class="form-control"
            placeholder="Choice Text"
          />
          <div class="input-group-text">
            <input
              type="checkbox"
              v-model="choice.is_correct"
            />
            Correct
          </div>
        </div>
        <button type="button" class="btn btn-link" @click="addChoice">{{ $t("addChoice") }}</button>
      </div>

      <!-- Correct Answer Field (for Text type) -->
      <div v-if="formData.type === 'TEXT'" class="mb-3">
        <label for="correctAnswer" class="form-label">{{ $t("correctAnswer") }}</label>
        <textarea
          v-model="formData.correctAnswer"
          class="form-control"
          rows="3"
        ></textarea>
      </div>

      <button class="btn btn-outline-accent" type="submit">{{ $t(mode) }}</button>
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
