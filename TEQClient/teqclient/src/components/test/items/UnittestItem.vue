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
  readonly: {
    type: Boolean,
    required: false,
    default: false,
  },
});

const model = defineModel({ required: true });
</script>

<template>
  <div class="unit">
    <div class="ms-1">{{ index + 1 }}.</div>
    <div class="in-out">
      <div class="input-group">
        <input
          type="text"
          class="form-control mb-0"
          :placeholder="$t('funInput')"
          aria-label="input"
          v-model="model.inTest"
          :readonly="readonly"
        />
        <span class="input-group-text mb-0"><i class="fa-solid fa-arrow-right"></i></span>
        <input
          type="text"
          class="form-control mb-0"
          :placeholder="$t('funOutput')"
          aria-label="output"
          v-model="model.outTest"
          :readonly="readonly"
        />
      </div>
    </div>
    <div class="btn-hover" v-if="count > 1" @click="onRemoved">
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
.in-out{
  width: 90%;
}
</style>
