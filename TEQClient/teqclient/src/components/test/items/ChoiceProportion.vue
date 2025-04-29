<script setup>

const formData = defineModel({required:true});

</script>

<template>
  <div
    class="col-md-6"
  >
    <div class="form-check form-switch">
      <input
        class="form-check-input"
        type="checkbox"
        role="switch"
        v-model="formData.allowProportion"
      />
      <label class="form-check-label" :title="$t('allowProportionHint')">{{
          $t("allowProportion")
        }}</label>
    </div>
  </div>
</template>

<style scoped>

</style>
