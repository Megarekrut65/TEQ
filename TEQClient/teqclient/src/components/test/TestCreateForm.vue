<script setup>
import FormWrapper from "@/components/FormWrapper.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";
import LoadingWindow from "@/components/LoadingWindow.vue";
import { testCreateApi } from "@/js/api/test.js";
import { errorAlert } from "@/js/utility/utility.js";

const props = defineProps({
    instance: {
        type: Object,
        required: false,
        default: () => ({
            title: "",
            description: "",
        }),
    },
});

const formData = ref(props.instance);

const router = useRouter();

const loading = ref(false);

const createTest = () => {
    return testCreateApi(formData.value).then((res) => {
        router.push({ name: "editor", params: { testId: res.id } });
    });
};

const onSubmit = () => {
    loading.value = true;

    createTest()
        .catch(errorAlert)
        .finally(() => {
            loading.value = false;
        });
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
                />
            </div>

            <button class="btn btn-outline-secondary" type="submit">{{ $t("create") }}</button>
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
