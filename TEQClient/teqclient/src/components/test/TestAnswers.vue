<script setup>
import ModalWindow from "@/components/ModalWindow.vue";
import LocalizedLink from "@/components/l10n/LocalizedLink.vue";
import { onMounted, onUnmounted, ref } from "vue";
import { answerCheckUpdateApi, answerTestGetListApi } from "@/js/api/answer.js";
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

const interval = ref(null);
onMounted(() => {
  interval.value = setInterval(refreshAnswers, 10000);
});

onUnmounted(() => {
  if (interval.value) {
    clearInterval(interval.value);
  }
});

const onCheck = (index, checked) => {
  const answer = answers.value[index];
  answer.checked = checked;
  answerCheckUpdateApi(answer.id, checked).catch(errorAlert);
};
</script>

<template>
  <ModalWindow v-model="model" size="large" margin-top="50px">
    <template v-slot:header>
      <h3 class="mb-0 mt-0">{{ $t("answers") }}</h3>
    </template>

    <div v-if="answers.length > 0" class="answer-table">
      <table class="table table-bordered table-striped table-responsive">
        <thead class="table-dark">
          <tr>
            <th class="text-center">#</th>
            <th>{{ $t("fullname") }}</th>
            <th>{{ $t("email") }}</th>
            <th>{{ $t("passDate") }}</th>
            <th>{{ $t("grade") }}</th>
            <th>{{ $t("autoCheckedTh") }}</th>
            <th><i class="fa-solid fa-handshake"></i></th>
            <th><i class="fa-solid fa-arrow-right"></i></th>
            <th><i class="fa-solid fa-eye"></i></th>
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
              <i
                v-if="answer.agree"
                class="fa-solid fa-handshake text-success"
                :title="$t('agreed')"
              ></i>
              <i v-else class="fa-solid fa-handshake text-danger" :title="$t('notAgreed')"></i>
            </td>
            <td>
              <LocalizedLink :to="`/answer/${answer.id}`" target="_blank">
                <i class="fa-solid fa-arrow-right" :title="$t('goTo')"></i
              ></LocalizedLink>
            </td>
            <td>
              <div
                class="btn-hover"
                :title="$t('published')"
                v-if="answer.checked"
                @click="() => onCheck(index, false)"
              >
                <i class="fa-solid fa-eye text-success"></i>
              </div>
              <div
                class="btn-hover"
                :title="$t('publishResultTh')"
                v-else
                @click="() => onCheck(index, true)"
              >
                <i class="fa-solid fa-eye-slash text-danger"></i>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>{{ $t("noUserAnswers") }}</div>
  </ModalWindow>
</template>

<style scoped>
.answer-table{
  max-height: 60vh;
  overflow-y: auto;
}
</style>
