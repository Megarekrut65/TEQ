<script setup>
import { getUser } from "@/js/utility/auth.js";
import { ref } from "vue";
import LocalizedLink from "@/components/l10n/LocalizedLink.vue";

const user = ref(getUser());
</script>

<template>
  <div class="max-w-xl mx-auto p-6 bg-white rounded-2xl shadow-md space-y-4">
    <h1 class="text-2xl font-bold text-gray-800 ps-4">{{ $t('accountTitle') }}</h1>

    <div class="ps-4">
      <p class="mb-1"><strong>{{ $t('fullname') }}:</strong> <span class="text-gray-700">{{ user.fullname }}</span></p>
      <p class="mb-1"><strong>{{ $t('email') }}:</strong> <span class="text-gray-700">{{ user.email }}</span></p>
    </div>

    <div class="pt-4 border-t border-gray-200 ps-4">
      <ul class="list-disc list-inside">
        <li>
          <LocalizedLink to="/account/tests" class="text-blue-600 hover:underline">{{ $t('myTests') }}</LocalizedLink>
        </li>
        <li>
          <LocalizedLink to="/account/answers" class="text-blue-600 hover:underline">{{ $t('myAnswers') }}</LocalizedLink>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
p {
  font-size: 1rem;
}
</style>
