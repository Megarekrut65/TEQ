<script setup>
defineProps({
  index: {
    type: Number,
    required: true,
  },
  count: {
    type: Number,
    required: true,
  },
  onRemoved: {
    type: Function,
    required: true,
  },
});

const model = defineModel({ required: true });
</script>

<template>
  <div class="unit">
    <div class="ms-1">{{ index + 1 }}.</div>
    <div>
      <div class="input-group">
        <input
          type="text"
          class="form-control mb-0"
          :placeholder="$t('funInput')"
          aria-label="input"
          v-model="model.inTest"
        />
        <span class="input-group-text mb-0"><i class="fa-solid fa-arrow-right"></i></span>
        <input
          type="text"
          class="form-control mb-0"
          :placeholder="$t('funOutput')"
          aria-label="output"
          v-model="model.outTest"
        />
      </div>
    </div>
    <div class="btn-hover" v-if="count !== 1" @click="onRemoved">
      <i class="fa-solid fa-trash-can"></i>
    </div>
  </div>
</template>

<style scoped>
.unit {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid rgb(242, 137, 63);
  padding: 5px;
  margin-top: 5px;
}
</style>
