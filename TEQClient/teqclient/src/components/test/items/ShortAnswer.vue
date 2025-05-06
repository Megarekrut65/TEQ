<script setup>
const formData = defineModel({ required: true });
</script>

<template>
  <div class="mb-3">
    <label for="correctAnswer" class="form-label">{{ $t("correctAnswer") }}</label>
    <input v-model.trim="formData.correctAnswer" class="form-control" maxlength="500" type="text" />
  </div>
</template>

<style scoped></style>
