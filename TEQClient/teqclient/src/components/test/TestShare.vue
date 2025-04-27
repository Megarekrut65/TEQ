<script setup>
import ModalWindow from "@/components/ModalWindow.vue";
import { useRouter } from "vue-router";
import { ref } from "vue";
import { copyToClipboard, errorAlert, successAlert } from "@/js/utility/utility.js";
import i18n from "@/i18n/index.js";
i18n.useT();

const model = defineModel({ required: true });
const activeModel = defineModel("active");

const router = useRouter();

const toUrl = (name, params, query = {}) => {
    const resolved = router.resolve({ name, params, query });
    return window.location.origin + resolved.fullPath;
};

const url = ref(toUrl("pass", { testId: model.value.id }));

const copy = () => {
    copyToClipboard(url.value)
        .then(() => {
            successAlert(i18n.t("copied"));
        })
        .catch(errorAlert);
};
</script>

<template>
    <ModalWindow v-model="activeModel">
        <template v-slot:header>
            <h2 class="mb-0 mt-0">{{ $t("share") }}</h2>
        </template>

        <p>{{ $t("shareExp") }}</p>

        <div class="form-check form-switch">
            <input
                class="form-check-input"
                type="checkbox"
                role="switch"
                v-model="model.isPublic"
            />
            <label class="form-check-label">{{ $t("isPublic") }}</label>
        </div>

        <div v-if="model.isPublic">
            <label class="form-label"
                >{{ $t("shareUrl") }} <i class="fa-solid fa-copy btn-hover" @click="copy"></i
            ></label>
            <input type="text" class="form-control" readonly v-model="url" />
        </div>
    </ModalWindow>
</template>

<style scoped></style>
