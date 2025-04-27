<script setup>
import { MULTIPLE, SINGLE, SHORT, FULL } from "@/js/types.js";
import { answerItemUpdateApi } from "@/js/api/answer.js";
import { errorAlert } from "@/js/utility/utility.js";

const props = defineProps({
    answerId: {
        type: String,
        required: true,
    },
    index: {
        type: Number,
        required: true,
    },
    readonly: {
        type: Boolean,
        required: false,
        default: false,
    },
    showCorrect: {
        type: Boolean,
        required: false,
        default: false,
    },
    autoCheck: {
        type: Boolean,
        required: false,
        default: false,
    },
    item: {
        type: Object,
        required: true,
    },
    isOwner: {
        type: Boolean,
        required: false,
        default: false,
    },
});

const formData = defineModel({ required: true });

const updateGrade = () => {
    answerItemUpdateApi(props.answerId, props.index - 1, formData.value).catch(errorAlert);
};
</script>

<template>
    <div class="card mt-3">
        <div class="card-body">
            <div class="d-flex justify-content-between">
                <label>{{ index }}. {{ item.text }}</label>
                <div v-if="isOwner" class="badge">
                    <label class="form-label text-dark"
                        >{{ $t("grade") }}({{ formData.grade }}/{{ item.grade }})</label
                    >
                    <input
                        @change="updateGrade"
                        class="form-control"
                        type="number"
                        v-model="formData.grade"
                    />
                </div>
                <div v-else-if="showCorrect" class="badge bg-secondary">
                    {{ formData.grade }}/{{ item.grade }}
                </div>
            </div>

            <div v-if="[SINGLE, MULTIPLE].includes(item.type)" class="mb-3">
                <label class="form-label">{{ $t("choices") }}</label>

                <div v-for="(choice, i) in item.choices" :key="choice">
                    <div class="form-check">
                        <input
                            v-if="[SINGLE].includes(item.type)"
                            class="form-check-input"
                            type="radio"
                            :name="`radio_${index}`"
                            v-model="formData.choices[0]"
                            :value="i"
                            :disabled="readonly"
                        />

                        <input
                            v-else
                            class="form-check-input"
                            type="checkbox"
                            v-model="formData.choices"
                            :value="i"
                            :disabled="readonly"
                        />

                        <label
                            :class="{
                                'form-check-label': true,
                                'text-success': showCorrect && choice.isCorrect,
                            }"
                        >
                            {{ choice.text
                            }}<i
                                v-if="showCorrect && choice.isCorrect"
                                class="fa-solid fa-check"
                            ></i>
                        </label>
                    </div>
                </div>
                <input
                    class="form-check-input hide"
                    type="radio"
                    :name="`radio_${index}`"
                    v-model="formData.choices[0]"
                    value="-1"
                />
            </div>

            <div v-if="[FULL, SHORT].includes(formData.type)" class="mb-3">
                <div v-if="showCorrect && autoCheck" class="badge text-dark bg-warning sim-badge">
                    {{ formData.similarity.toFixed(1) }}%
                </div>
                <textarea
                    v-if="[FULL].includes(formData.type)"
                    v-model="formData.answer"
                    class="form-control"
                    rows="3"
                    :readonly="readonly"
                    maxlength="5000"
                ></textarea>
                <input
                    v-else
                    v-model="formData.answer"
                    class="form-control"
                    type="text"
                    :readonly="readonly"
                />
                <div v-if="showCorrect && item.correctAnswer">
                    <span class="text-success">{{ $t("answer") }}</span>
                    <p>{{ item.correctAnswer }}</p>
                </div>
            </div>
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

.hide {
    display: none;
}
.badge {
    height: min-content;
}
</style>
