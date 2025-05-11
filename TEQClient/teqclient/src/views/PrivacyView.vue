<template>
  <div class="container py-5">
    <h1 class="mb-4 text-center">{{ $t("privacy.title") }}</h1>
    <div class="card shadow-sm">
      <div class="card-body">
        <p v-for="(paragraph, index) in $tm('privacy.content')" :key="index" class="mb-3">
          {{ paragraph }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.card-body {
  font-size: 1rem;
  line-height: 1.6;
}
</style>
