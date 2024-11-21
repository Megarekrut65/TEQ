<script setup>
import FormWrapper from "@/components/FormWrapper.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";
import LoadingWindow from "@/components/LoadingWindow.vue";
import { testCreateApi, testUpdateApi } from "@/js/api/test.js";
import { errorAlert } from "@/js/utility/utility.js";

const props = defineProps({
  instance: {
    type: Object,
    required: false,
    default: () => {
      return {
        title: "",
        description: "",
        isPublic: false
      };
    }
  },
  mode: {
    type: String,
    required: false,
    default: "create"
  }
});

const formData = ref(props.instance);

const router = useRouter();

const loading = ref(false);

const createTest = () => {
  return testCreateApi(formData.value).then((res) => {
    router.push({ name: "editor", params: { testId: res.id } });
  });
};

const updateTest = () => {
  return testUpdateApi(props.instance.id, formData.value).then((res) => {
    formData.value = res;
  });
};

const api = props.mode === "create" ? createTest : updateTest;

const onSubmit = () => {
  loading.value = true;

  api().catch(errorAlert).finally(() => {
    loading.value = false;
  });
};
</script>

<template>
  <LoadingWindow v-if="loading" />
  <FormWrapper :title="$t(mode)+ ' '+$t('test')">
    <form @submit.prevent="onSubmit">
      <div>
        <label class="form-label" for="title">{{ $t("title") }}</label>
        <input
          v-model.trim="formData.title"
          type="text"
          class="form-control"
          maxlength="255"
          required
        />
      </div>
      <div>
        <label class="form-label" for="description">{{ $t("description") }}</label>
        <textarea
          v-model.trim="formData.description"
          class="form-control"
          maxlength="1000"
        />
      </div>

      <div class="form-check">
        <input v-model="formData.isPublic" class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
        <label class="form-check-label" for="flexCheckDefault">
          {{ $t("isPublic") }}
        </label>
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
