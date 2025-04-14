<script setup>

import { ref } from "vue";
import { testDeleteApi, testListApi } from "@/js/api/test.js";
import { errorAlert, truncate } from "@/js/utility/utility.js";
import LoadingWindow from "@/components/LoadingWindow.vue";
import LocalizedLink from "@/components/l10n/LocalizedLink.vue";
import QuestionWindow from "@/components/QuestionWindow.vue";

const tests = ref([]);

const loading = ref(true);

testListApi().then(res => {
  tests.value = res.results;
  console.log(res);
}).catch(errorAlert).finally(() => {
  loading.value = false;
});

const currentTest = ref(null);
const removeActive = ref(false);

const removeTest = () => {
  if (!currentTest.value) return;

  const id = currentTest.value.id;
  loading.value = true;

  testDeleteApi(id).then(() => {
    tests.value = tests.value.filter((item) => item.id !== id);
  }).catch(errorAlert).finally(() => {
    loading.value = false;
    currentTest.value = null;
  });
};

</script>

<template>
  <QuestionWindow v-model="removeActive" :on-success="removeTest"
                  :message="$t('removeMsg')" />
  <LoadingWindow v-if="loading" />
  <div v-if="tests.length>0" class="scroll">
    <LocalizedLink to="editor/new"><i class="fa fa-plus"></i></LocalizedLink>
    <table class="table table-bordered table-striped">
      <thead class="table-dark">
      <tr>
        <th class="text-center">#</th>
        <th>{{ $t("title") }}</th>
        <th>{{ $t("description") }}</th>
        <th>{{ $t("isPublic") }}</th>
        <th>{{ $t("createdDate") }}</th>
        <th>{{ $t("goTo") }}</th>
        <th>{{ $t("remove") }}</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(test, index) in tests" :key="index">
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
.scroll{
  overflow-x: auto;
}
</style>
