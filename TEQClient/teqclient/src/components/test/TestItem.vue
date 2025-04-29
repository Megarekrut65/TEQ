<script setup>
import FormWrapper from "@/components/FormWrapper.vue";
import { errorAlert } from "@/js/utility/utility.js";
import { MULTIPLE, SINGLE, SHORT, FULL, TYPES, SCRIPT } from "@/js/types.js";
import { defaultChoices } from "@/js/data-types.js";
import DotsMenu from "@/components/DotsMenu.vue";
import { copyObject, pasteObject } from "@/js/utility/clipboard.js";
import ChoiceProportion from "@/components/test/items/ChoiceProportion.vue";
import ChoiceAnswers from "@/components/test/items/ChoiceAnswers.vue";
import ShortAnswer from "@/components/test/items/ShortAnswer.vue";
import FullAnswer from "@/components/test/items/FullAnswer.vue";
import AnswerSimilarity from "@/components/test/items/AnswerSimilarity.vue";
import ScriptAnswer from "@/components/test/items/ScriptAnswer.vue";
import { languages } from "@/js/languages.js";

const props = defineProps({
    index: {
        type: Number,
        required: true,
    },
    testId: {
        type: String,
        required: true,
    },
    autoCheck: {
        type: Boolean,
        required: true,
    },
    onItemRemoved: {
        type: Function,
        required: true,
    },
    updateApi: {
        type: Function,
        required: true,
    },
    onItemPaste: {
        type: Function,
        required: true,
    },
    openPool: {
        type: Function,
        required: false,
        default: null,
    },
});

const formData = defineModel({ required: true });

const onUpdate = () => {
    if (
        [SINGLE, MULTIPLE].includes(formData.value.type) &&
        (formData.value.choices == null || formData.value.choices.length === 0)
    ) {
        formData.value.choices = defaultChoices();
    }

    if ([SCRIPT].includes(formData.value.type) && !formData.value.language) {
        formData.value.language = languages[0].type;
    }

    if ([SCRIPT, SHORT, FULL].includes(formData.value.type) && !formData.value.minSimilarPercent) {
        formData.value.minSimilarPercent = 99;
    }

    props.updateApi(props.testId, props.index - 1, formData.value).catch(errorAlert);
};

const onAddToPool = () => {
    props.openPool(formData.value, true);
};
const onPasteFromPool = () => {
    props.openPool(formData.value, false);
};

const onCopy = () => {
    copyObject("testItem", formData.value);
};
const onPaste = () => {
    const data = pasteObject("testItem");
    if (data) {
        formData.value = data;
    }
};

const onPasteNew = () => {
    const data = pasteObject("testItem");
    if (data) {
        props.onItemPaste(data);
    }
};
</script>

<template>
    <FormWrapper class="mb-3">
        <form @change="onUpdate">
            <div>
                <div class="float-right">
                    <DotsMenu>
                        <div class="dropdown-item" @click="onItemRemoved">{{ $t("delete") }}</div>
                        <div class="dropdown-item" @click="onCopy">{{ $t("copy") }}</div>
                        <div class="dropdown-item" @click="onPaste">{{ $t("paste") }}</div>
                        <div class="dropdown-item" @click="onPasteNew">{{ $t("pasteAsNew") }}</div>
                        <div class="dropdown-item" @click="onPasteFromPool" v-if="openPool">
                            {{ $t("pasteFromPool") }}
                        </div>
                        <div class="dropdown-item" @click="onAddToPool" v-if="openPool">
                            {{ $t("addToPool") }}
                        </div>
                    </DotsMenu>
                </div>
                <label class="form-label" for="text">{{ index }}. {{ formData.text }}</label>
                <input
                    v-model.trim="formData.text"
                    type="text"
                    class="form-control"
                    :placeholder="$t('questionText')"
                    required
                />
            </div>

            <div>
                <label class="form-label" for="type">{{ $t("type") }}</label>
                <select v-model="formData.type" class="form-select" required>
                    <option
                        v-for="(type, index) in TYPES"
                        :value="type"
                        :key="type"
                        :selected="index === 0"
                    >
                        {{ $t(type.toLowerCase()) }}
                    </option>
                </select>
            </div>

            <div class="row mb-3">
                <ChoiceProportion
                    v-if="[SINGLE, MULTIPLE].includes(formData.type) && autoCheck"
                    v-model="formData"
                />

                <div class="col-md-6">
                    <div class="input-group">
                        <span class="input-group-text" id="basic-grade">{{ $t("grade") }}</span>
                        <input
                            v-model.trim="formData.grade"
                            type="number"
                            min="0"
                            class="form-control mb-0"
                            required
                            aria-describedby="basic-grade"
                        />
                    </div>
                </div>
            </div>

            <ChoiceAnswers
                v-if="[SINGLE, MULTIPLE].includes(formData.type)"
                v-model="formData"
                :on-update="onUpdate"
            />

            <ShortAnswer v-if="[SHORT].includes(formData.type)" v-model="formData" />
            <FullAnswer v-if="[FULL].includes(formData.type)" v-model="formData" />
            <ScriptAnswer v-if="[SCRIPT].includes(formData.type)" v-model="formData" />

            <AnswerSimilarity
                v-if="[SHORT, FULL, SCRIPT].includes(formData.type) && autoCheck"
                v-model="formData"
            />
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
