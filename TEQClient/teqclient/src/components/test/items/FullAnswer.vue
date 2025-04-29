<script setup>

const formData = defineModel({required:true});

</script>

<template>
  <div  class="mb-3">
    <label for="correctAnswer" class="form-label">{{ $t("correctAnswer") }}</label>
    <textarea
      v-model="formData.correctAnswer"
      class="form-control"
      rows="3"
      maxlength="5000"
    ></textarea>
  </div>
</template>

<style scoped>

</style>
