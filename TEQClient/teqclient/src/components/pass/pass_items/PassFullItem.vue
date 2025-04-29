<script setup>
defineProps({
  readonly: {
    type: Boolean,
    required: true,
  },
});

const formData = defineModel({ required: true });
</script>

<template>
  <textarea
    v-model="formData.answer"
    class="form-control"
    rows="3"
    :readonly="readonly"
    maxlength="5000"
  ></textarea>
</template>

<style scoped></style>
