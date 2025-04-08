<script setup>
import FormWrapper from "@/components/FormWrapper.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";
import LoadingWindow from "@/components/LoadingWindow.vue";
import { testCreateApi, testUpdateApi } from "@/js/api/test.js";
import { errorAlert } from "@/js/utility/utility.js";
import TestItem from "@/components/test/TestItem.vue";
import { itemCreateApi, itemDeleteApi } from "@/js/api/item.js";
import { defaultAnswer } from "@/js/data-types.js";

const props = defineProps({
    instance: {
        type: Object,
        required: false,
        default: () => {
            return {
                title: "",
                description: "",
                isPublic: false,
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

const addNewAnswer = () => {
    itemCreateApi(defaultAnswer(formData.value.id))
        .then((res) => {
            formData.value.items.push(res);
        })
        .catch(errorAlert);
};

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

    api()
        .catch(errorAlert)
        .finally(() => {
            loading.value = false;
        });
};

const onItemRemoved = (index) => {
    if (index < 0 || index >= formData.value.items.length) return;

    formData.value.items.splice(index, 1);
    itemDeleteApi(formData.value.id, index).catch(errorAlert);
};
</script>

<template>
    <LoadingWindow v-if="loading" />
    <FormWrapper :title="$t(mode) + ' ' + $t('test')">
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
                <input
                    v-model="formData.isPublic"
                    class="form-check-input"
                    type="checkbox"
                    value=""
                    id="flexCheckDefault"
                />
                <label class="form-check-label" for="flexCheckDefault">
                    {{ $t("isPublic") }}
                </label>
            </div>

            <button class="btn btn-outline-secondary" type="submit">{{ $t(mode) }}</button>
        </form>
    </FormWrapper>
    <div v-if="mode !== 'create'">
        <div class="mt-3">
            <TestItem
                v-for="(item, index) in formData.items"
                :key="index"
                :index="index + 1"
                v-model="formData.items[index]"
                :on-item-removed="() => onItemRemoved(index)"
                :test-id="formData.id"
            />
        </div>
        <div class="d-flex justify-content-center">
            <img src="@/assets/images/plus.png" class="btn-img" alt="plus" @click="addNewAnswer" />
        </div>
    </div>
</template>

<style scoped>
button {
    margin: 0;
}

form {
    margin-bottom: 0;
}
</style>
