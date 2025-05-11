<script setup></script>

<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 mb-4">
        <div class="card shadow-sm">
          <div class="card-body">
            <h3 class="card-title mt-1">{{ $t("infoTitle") }}</h3>
            <p class="m-0"><i class="fa-solid fa-phone"></i> +380 (123) 456-789</p>
            <p class="m-0"><i class="fa-solid fa-envelope"></i> bandalak28@knu.ua</p>
            <p class="m-0"><i class="fa-solid fa-map-pin"></i> {{ $t("address") }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
img {
  width: 100%;
}
</style>
