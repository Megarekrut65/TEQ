<script setup>
import { computed } from "vue";
import { alertBus } from "@/js/utility/alert-bus.js";

const alerts = computed(() => alertBus.alerts);
</script>

<template>
  <div class="alert-window">
    <div v-for="alert in alerts" :key="alert" :class="`alert alert-${alert.alert}`" role="alert">
      <div>{{ alert.msg }}</div>
      <i class="fa-solid fa-xmark icon-btn" @click="() => alertBus.closeAlert(alert)"></i>
    </div>
  </div>
</template>

<style scoped>
.alert-window {
  position: fixed;
  bottom: 0;
  right: 0;
  width: 100%;
  z-index: 1000;
}

.alert {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.icon-btn:hover {
  cursor: pointer;
  opacity: 0.8;
}
</style>
