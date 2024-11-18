<script setup>
import FormWrapper from "@/components/FormWrapper.vue";
import { ref } from "vue";

const formData = ref({
  email: "",
  password: ""
});

const onSubmit = () => {
};
</script>

<template>
  <FormWrapper :title="$t('singIn')">
    <form @submit.prevent="onSubmit">
      <div>
        <label class="form-label" for="email">{{ $t("email") }}</label>
        <input
          v-model.trim="formData.email"
          type="email"
          class="form-control"
          maxlength="255"
          required
        />
      </div>

      <div>
        <label class="form-label" for="password">{{ $t("password") }}</label>
        <input
          v-model.trim="formData.password"
          type="password"
          class="form-control"
          maxlength="1000"
          required
        />
      </div>

      <button class="btn btn-outline-accent" type="submit">{{ $t("singIn") }}</button>

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
