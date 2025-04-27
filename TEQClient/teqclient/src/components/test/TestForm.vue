<script setup>
import FormWrapper from "@/components/FormWrapper.vue";
import { ref } from "vue";

import { testUpdateApi } from "@/js/api/test.js";
import { errorAlert } from "@/js/utility/utility.js";
import TestItem from "@/components/test/TestItem.vue";
import { itemCreateApi, itemDeleteApi, itemUpdateApi } from "@/js/api/item.js";
import { defaultAnswer } from "@/js/data-types.js";
import LocalizedLink from "@/components/l10n/LocalizedLink.vue";
import MemberForm from "@/components/test/MemberForm.vue";
import TestSettings from "@/components/test/TestSettings.vue";
import TestShare from "@/components/test/TestShare.vue";
import TestAnswers from "@/components/test/TestAnswers.vue";
import PoolWindow from "@/components/pool/PoolWindow.vue";

const props = defineProps({
    instance: {
        type: Object,
        required: true,
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

const updateTest = () => {
    if (formData.value.title === "") return;

    testUpdateApi(props.instance.id, formData.value).then(res=>{
      formData.value.canShare = res.canShare;
      formData.value.isPublic = res.isPublic;
    }).catch(errorAlert);

};

const onItemRemoved = (index) => {
    if (index < 0 || index >= formData.value.items.length) return;

    formData.value.items.splice(index, 1);
    itemDeleteApi(formData.value.id, index).catch(errorAlert);
};

const memberActive = ref(false);
const settingsActive = ref(false);
const shareActive = ref(false);
const answerActive = ref(false);
const poolActive = ref(false);

const onItemPaste = (data) => {
    data.testId = formData.value.id;

    itemCreateApi(data)
        .then((res) => {
            formData.value.items.push(res);
        })
        .catch(errorAlert);
};

const poolItem = ref(null);
const poolPasteMode = ref(true);
const onOpenPool = (item, pasteMode) => {
    poolActive.value = true;
    poolPasteMode.value = pasteMode;
    poolItem.value = item;
};
</script>

<template>
    <MemberForm v-model="memberActive" :test-id="formData.id"></MemberForm>
    <TestSettings v-model="formData" v-model:active="settingsActive" @change="updateTest" />
    <TestShare v-model="formData" v-model:active="shareActive" @change="updateTest" />
    <TestAnswers :test-id="formData.id" v-model="answerActive"></TestAnswers>
    <PoolWindow
        v-model="poolActive"
        v-model:item="poolItem"
        :paste-mode="poolPasteMode"
        :add-selected="onItemPaste"
    ></PoolWindow>

    <FormWrapper :title="formData.title" show-menu>
        <template v-slot:menu>
            <a class="dropdown-item" href="#" @click="shareActive = true">
                {{ $t("share") }}
            </a>

            <LocalizedLink class="dropdown-item" :to="`pass/${formData.id}`" target="_blank">
                {{ $t("pass") }}
            </LocalizedLink>
            <a class="dropdown-item" href="#" @click="memberActive = true">
                {{ $t("members") }}
            </a>
            <a class="dropdown-item" href="#" @click="answerActive = true">
                {{ $t("answers") }}
            </a>
            <a class="dropdown-item" href="#" @click="settingsActive = true">
                {{ $t("settings") }}
            </a>
        </template>
        <form @change="updateTest">
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
        </form>
    </FormWrapper>
    <div>
        <div class="mt-3">
            <TestItem
                v-for="(item, index) in formData.items"
                :key="index"
                :index="index + 1"
                v-model="formData.items[index]"
                :on-item-removed="() => onItemRemoved(index)"
                :test-id="formData.id"
                :auto-check="formData.autoCheck"
                :update-api="itemUpdateApi"
                :on-item-paste="onItemPaste"
                :open-pool="onOpenPool"
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
