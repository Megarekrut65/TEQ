<script setup>
import LoginForm from "@/components/LoginForm.vue";
import RegisterForm from "@/components/RegisterForm.vue";
</script>

<template>
  <div class="row">
    <div class="col-0 col-md-0 col-xl-2"></div>
    <div class="col-12 col-md-6 col-xl-4 mt-2"><LoginForm /></div>
    <div class="col-12 col-md-6 col-xl-4 mt-2"><RegisterForm /></div>
    <div class="col-0 col-md-0 col-xl-2"></div>
  </div>
</template>

<style scoped></style>
