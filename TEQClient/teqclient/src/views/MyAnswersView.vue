<script setup>
import { ref } from "vue";
import { errorAlert } from "@/js/utility/utility.js";
import LoadingWindow from "@/components/LoadingWindow.vue";
import LocalizedLink from "@/components/l10n/LocalizedLink.vue";
import { answerGetListApi } from "@/js/api/answer.js";
import PaginationPanel from "@/components/PaginationPanel.vue";

const answers = ref([]);

const loading = ref(true);

const page = ref(0);
const totalPages = ref(0);

const updatePage = (number) => {
  answerGetListApi(number)
    .then((res) => {
      answers.value = res.results;
      page.value = number;
      totalPages.value = Math.ceil(res.count / 24);
    })
    .catch(errorAlert)
    .finally(() => {
      loading.value = false;
    });
};

updatePage(1);
</script>

<template>
  <LoadingWindow v-if="loading" />
  <div v-if="answers.length > 0">
    <table class="table table-bordered table-striped">
      <thead class="table-dark">
        <tr>
          <th class="text-center">#</th>
          <th class="test-title">{{ $t("test") }}</th>
          <th>{{ $t("passDate") }}</th>
          <th>{{ $t("grade") }}</th>
          <th>{{ $t("goTo") }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(answer, index) in answers" :key="index">
          <td class="text-center">{{ index + 1 }}</td>
          <td>
            <LocalizedLink :to="`/pass/${answer.test.id}`">{{ answer.test.title }}</LocalizedLink>
          </td>
          <td>{{ new Date(answer.passDate).toLocaleString() }}</td>
          <td v-if="answer.checked">{{ answer.grade }}/{{ answer.maxGrade }}</td>
          <td v-else>-/-</td>
          <td>
            <LocalizedLink :to="`/answer/${answer.id}`">{{ $t("goTo") }}</LocalizedLink>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <div v-else>{{ $t("noAnswers") }}</div>

  <div class="row mt-4" v-if="totalPages > 0">
    <PaginationPanel
      :on-page-change="updatePage"
      :total-pages="totalPages"
      :current-page="page"
    ></PaginationPanel>
  </div>
</template>

<style scoped>
.test-title {
  text-transform: capitalize;
}
</style>
