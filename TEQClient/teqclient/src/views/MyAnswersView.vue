<script setup>
import { ref } from "vue";
import { errorAlert } from "@/js/utility/utility.js";
import LoadingWindow from "@/components/LoadingWindow.vue";
import LocalizedLink from "@/components/l10n/LocalizedLink.vue";
import { answerGetListApi } from "@/js/api/answer.js";

const answers = ref([]);

const loading = ref(true);

answerGetListApi()
    .then((res) => {
        answers.value = res.results;
        console.log(res);
    })
    .catch(errorAlert)
    .finally(() => {
        loading.value = false;
    });
</script>

<template>
    <LoadingWindow v-if="loading" />
    <div v-if="answers.length > 0">
        <table class="table table-bordered table-striped">
            <thead class="table-dark">
                <tr>
                    <th class="text-center">#</th>
                    <th>{{ $t("title") }}</th>
                    <th>{{ $t("passDate") }}</th>
                    <th>{{ $t("grade") }}</th>
                    <th>{{ $t("goTo") }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(answer, index) in answers" :key="index">
                    <td class="text-center">{{ index + 1 }}</td>
                    <td>
                        <LocalizedLink :to="`/pass/${answer.test.id}`">{{
                            answer.test.title
                        }}</LocalizedLink>
                    </td>
                    <td>{{ new Date(answer.passDate).toLocaleString() }}</td>
                    <td>{{ answer.grade }}/{{ answer.maxGrade }}</td>
                    <td>
                        <LocalizedLink :to="`/answer/${answer.id}`">{{ $t("goTo") }}</LocalizedLink>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <div v-else>{{ $t("noAnswers") }}</div>
</template>

<style scoped></style>
