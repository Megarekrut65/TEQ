<script setup>

import { ref } from "vue";
import { errorAlert, truncate } from "@/js/utility/utility.js";
import LoadingWindow from "@/components/LoadingWindow.vue";
import LocalizedLink from "@/components/l10n/LocalizedLink.vue";
import { answerGetListApi } from "@/js/api/answer.js";

const answers = ref([]);

const loading = ref(true);

answerGetListApi().then(res => {
  answers.value = res.results;
  console.log(res);
}).catch(errorAlert).finally(() => {
  loading.value = false;
});


</script>

<template>
  <LoadingWindow v-if="loading" />
  <div v-if="answers.length>0">
    <LocalizedLink to="editor/new"><i class="fa fa-plus"></i></LocalizedLink>
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
      <tr v-for="(test, index) in answers" :key="index">
        <td class="text-center">{{ index + 1 }}</td>
        <td>
          <LocalizedLink :to="`/editor/${test.id}`">{{ test.title }}</LocalizedLink>
        </td>
        <td>{{ truncate(test.description) }}</td>
        <td>{{ test.isPublic ? $t("yes") : $t("no") }}</td>
        <td>{{ new Date(test.createdDate).toLocaleString() }}</td>
        <td>
          <LocalizedLink :to="`/editor/${test.id}`">{{ $t("goTo") }}</LocalizedLink>
        </td>
        <td>
          <a href="#" @click="removeActive=true; currentTest=test">{{ $t("remove") }}</a>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
  <div v-else>{{ $t("noTests") }}
    <LocalizedLink to="editor/new">{{ $t("createOne") }}?</LocalizedLink>
  </div>

</template>

<style scoped>

</style>
