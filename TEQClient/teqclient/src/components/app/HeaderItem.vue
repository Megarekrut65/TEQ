<script setup>

import Menu from "@/components/app/MenuItem.vue";

import { ref, onMounted, onUnmounted } from "vue";

const isFixedTop = ref(false);

const initScrollNav = () => {
  isFixedTop.value = window.scrollY >= 100;
};

onMounted(() => {
  window.addEventListener("scroll", initScrollNav);
  initScrollNav(); // Ensure the header state is updated on mount
});

onUnmounted(() => {
  window.removeEventListener("scroll", initScrollNav);
});
</script>

<template>
  <div id="header-wrap">
    <header id="header" :class="{ 'fixed-top': isFixedTop }">
      <div class="container-fluid">
        <div class="row">
          <div class="col-md-2 logo-col">
            <div class="main-logo">
              <RouterLink to="/">
                <img src="@/assets/images/main-logo.png" alt="logo" />
              </RouterLink>
            </div>
          </div>

          <div class="col-md-10">
            <Menu />
          </div>
        </div>
      </div>
    </header>
  </div>
</template>

<style scoped>

</style>
