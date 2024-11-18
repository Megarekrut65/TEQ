<script setup>
import FormWrapper from "@/components/FormWrapper.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { register } from "@/js/utility/auth.js";
import { errorAlert } from "@/js/utility/utility.js";
import LoadingWindow from "@/components/LoadingWindow.vue";

const formData = ref({
  title: "",
  description: "",
  isPublic: false
});

const router = useRouter();

const loading = ref(false);

const onSubmit = () => {
  // register(formData.value)
  //   .then(() => {
  //     router.push("/");
  //   })
  //   .catch(errorAlert)
  //   .finally(() => {
  //     loading.value = false;
  //   });
};
</script>

<template>
  <LoadingWindow v-if="loading" />
  <FormWrapper :title="$t('createTest')">
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
          required
        />
      </div>

      <div class="form-check">
        <input v-model="formData.isPublic" class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
        <label class="form-check-label" for="flexCheckDefault">
          {{ $t("isPublic") }}
        </label>
      </div>


      <button class="btn btn-outline-accent" type="submit">{{ $t("create") }}</button>

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
