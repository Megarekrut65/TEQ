<script setup>
import { RouterView } from "vue-router";
import AlertWindow from "@/components/AlertWindow.vue";
import Footer from "@/components/app/FooterItem.vue";
import Header from "@/components/app/HeaderItem.vue";
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
