<script setup>
import { RouterView } from "vue-router";
import AlertWindow from "@/components/AlertWindow.vue";
import Footer from "@/components/app/Footer.vue";
import Header from "@/components/app/Header.vue";
</script>

<template>
  <AlertWindow />
  <Header />

  <section>
    <div class="container page">
      <RouterView />
    </div>
  </section>

  <Footer />
</template>
