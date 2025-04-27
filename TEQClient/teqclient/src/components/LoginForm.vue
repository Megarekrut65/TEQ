<script setup>
import FormWrapper from "@/components/FormWrapper.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { login } from "@/js/utility/auth.js";
import { errorAlert } from "@/js/utility/utility.js";
import LoadingWindow from "@/components/LoadingWindow.vue";

const formData = ref({
    email: "",
    password: "",
});

const router = useRouter();

const loading = ref(false);

const onSubmit = () => {
    loading.value = true;

    login(formData.value)
        .then(() => {
            router.push({ name: "home" });
        })
        .catch(errorAlert)
        .finally(() => {
            loading.value = false;
        });
};
</script>

<template>
    <LoadingWindow v-if="loading" />
    <FormWrapper :title="$t('signIn')">
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

            <button class="btn btn-outline-accent" type="submit">{{ $t("signIn") }}</button>
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
