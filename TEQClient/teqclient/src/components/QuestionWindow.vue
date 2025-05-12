<script setup>
import ModalWindow from "@/components/ModalWindow.vue";

const props = defineProps({
  message: {
    type: String,
    required: false,
    default: "",
  },
  onSuccess: {
    type: Function,
    required: true,
  },
  onCancel: {
    type: Function,
    required: false,
    default: () => {},
  },
});

const model = defineModel({ default: false });

const submit = () => {
  props.onSuccess();
  model.value = false;
};
</script>

<template>
  <ModalWindow v-model="model" :on-closed="onCancel">
    <p>{{ message }}</p>
    <button
      type="button"
      class="btn btn-outline-secondary"
      data-dismiss="modal"
      @click="
        onCancel();
        model = false;
      "
    >
      {{ $t("cancel") }}
    </button>
    <button type="button" class="btn btn-outline-primary" @click="submit">
      {{ $t("submit") }}
    </button>
  </ModalWindow>
</template>
