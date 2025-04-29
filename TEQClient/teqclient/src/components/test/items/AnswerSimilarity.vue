<script setup>

const formData = defineModel({required:true});

</script>

<template>
  <div  class="mb-3">
    <label class="form-label" for="text" :title="$t('minSimilarHnt')">{{
        $t("minSimilar")
      }}</label>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-percent">%</span>
      <input
        v-model.number="formData.minSimilarPercent"
        type="number"
        min="0"
        max="100"
        class="form-control mb-0"
        required
        value="90"
        aria-describedby="basic-percent"
      />
    </div>
  </div>
</template>

<style scoped>

</style>
