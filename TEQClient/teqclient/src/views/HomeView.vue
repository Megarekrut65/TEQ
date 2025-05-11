<script setup></script>

<template>
  <div class="container mt-4">
    <div class="row mt-4">
      <div class="col-12 col-md-6 mt-4">
        <img src="@/assets/images/big-log.png" alt="Logo" />
      </div>
      <div class="col-12 col-md-6 mt-4">
        <span class="text-secondary">{{ $t("appName") }} </span> — {{ $t("aboutApp") }}
      </div>
    </div>
  </div>
</template>
<style scoped>
img {
  width: 100%;
}
</style>
