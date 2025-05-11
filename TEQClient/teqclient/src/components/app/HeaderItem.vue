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
  <div class="wrapper">
    <header id="header" :class="{ 'fixed-top': isFixedTop }">
      <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
          <div class="main-logo navbar-brand">
            <RouterLink to="/">
              <img src="@/assets/images/main-logo.png" alt="logo" />
            </RouterLink>
          </div>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <Menu />
        </div>
      </nav>
    </header>
  </div>
</template>

<style scoped>
.wrapper {
  margin-bottom: 50px;
}
</style>
