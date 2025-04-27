<script setup>
import ModalWindow from "@/components/ModalWindow.vue";

const model = defineModel({ required: true });
const activeModel = defineModel("active");
</script>

<template>
    <ModalWindow v-model="activeModel">
        <template v-slot:header>
            <h2 class="mb-0 mt-0">{{ $t("settings") }}</h2>
        </template>

        <div class="form-check form-switch">
            <input
                class="form-check-input"
                type="checkbox"
                role="switch"
                :title="$t('public')"
                v-model="model.isPublic"
            />
            <label class="form-check-label">{{ $t("isPublic") }}</label>
        </div>
        <div class="form-check form-switch">
            <input
                class="form-check-input"
                type="checkbox"
                role="switch"
                v-model="model.showCorrect"
            />
            <label class="form-check-label" :title="$t('correctHint')">{{
                $t("showCorrect")
            }}</label>
        </div>
        <div class="form-check form-switch">
            <input
                class="form-check-input"
                type="checkbox"
                role="switch"
                v-model="model.autoCheck"
            />
            <label class="form-check-label" :title="$t('autoHint')">{{ $t("autoCheck") }}</label>
        </div>
        <div class="form-check form-switch" v-if="model.autoCheck">
            <input
                class="form-check-input"
                type="checkbox"
                role="switch"
                v-model="model.showResult"
            />
            <label class="form-check-label" :title="$t('resultHint')">{{ $t("showResult") }}</label>
        </div>
    </ModalWindow>
</template>

<style scoped></style>
