<script setup>
import ModalWindow from "@/components/ModalWindow.vue";
import LocalizedLink from "@/components/l10n/LocalizedLink.vue";
import { ref } from "vue";
import { answerTestGetListApi } from "@/js/api/answer.js";
import { errorAlert } from "@/js/utility/utility.js";

const props = defineProps({
  testId: {
    type: String,
    required: true,
  },
});

const model = defineModel({ required: true });

const answers = ref([]);

const refreshAnswers = () => {
  answerTestGetListApi(props.testId)
    .then((res) => {
      answers.value = res.results;
    })
    .catch(errorAlert);
};

refreshAnswers();

setInterval(refreshAnswers, 10000);
</script>

<template>
  <ModalWindow v-model="model" size="large">
    <template v-slot:header>
      <h3 class="mb-0 mt-0">{{ $t("answers") }}</h3>
    </template>

    <div v-if="answers.length > 0">
      <table class="table table-bordered table-striped table-responsive">
        <thead class="table-dark">
          <tr>
            <th class="text-center">#</th>
            <th>{{ $t("fullname") }}</th>
            <th>{{ $t("email") }}</th>
            <th>{{ $t("passDate") }}</th>
            <th>{{ $t("grade") }}</th>
            <th>{{ $t("autoCheckedTh") }}</th>
            <th>{{ $t("goTo") }}</th>
            <th>{{ $t("publishResultTh") }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(answer, index) in answers" :key="index">
            <td class="text-center">{{ index + 1 }}</td>
            <td>{{ answer.owner.fullname }}</td>
            <td>{{ answer.owner.email }}</td>
            <td>{{ new Date(answer.passDate).toLocaleString() }}</td>
            <td>{{ answer.grade.toFixed(2) }}/{{ answer.maxGrade.toFixed(2) }}</td>
            <td>{{ answer.autoChecked ? $t("yes") : $t("no") }}</td>
            <td>
              <LocalizedLink :to="`/answer/${answer.id}`" target="_blank">{{
                $t("goTo")
              }}</LocalizedLink>
            </td>
            <td>
              <a href="#">{{ $t("publish") }}</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>{{ $t("noUserAnswers") }}</div>
  </ModalWindow>
</template>

<style scoped></style>
