<script setup>
const props = defineProps({
  message: {
    type: String,
    required: false,
    default: ""
  },
  onSuccess: {
    type: Function,
    required: true
  },
  onCancel: {
    type: Function,
    required: false,
    default: () => {
    }
  }
});

const model = defineModel({ default: false });

const submit = () => {
  props.onSuccess();
  model.value = false;
};

const cancel = () => {
  props.onCancel();
  model.value = false;
};
</script>

<template>
  <div class="modal-window" v-if="model">
    <div class="modal show" style="display: block;">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-body">
            {{ message }}
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-outline-secondary" data-dismiss="modal" @click="cancel">
              {{ $t("cancel") }}
            </button>
            <button type="button" class="btn btn-outline-primary" @click="submit">{{ $t("submit") }}</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal-window {
  position: fixed;
  z-index: 2000;

  left: 0;
  top: 0;

  background-color: #0000001f;
  width: 100%;
  height: 100%;
}
</style>
