<script setup>
import { computed } from "vue";

const props = defineProps({
  onClosed: {
    type: Function,
    required: false,
    default: () => {
    }
  },
  marginTop:{
    type: String,
    required: false,
    default: "100px"
  },
  zIndex:{
    type: Number,
    required: false,
    default: 1
  }
});

const zIndex = computed(()=>props.zIndex + 10000);

const model = defineModel({ default: false });


const close = () => {
  props.onClosed();
  model.value = false;
};
</script>

<template>
  <div class="modal-window" v-if="model">
    <div class="modal-inner pt-5 ">
  <div class="row">
    <div class="col-0 col-sm-1 col-md-2 col-lg-3 col-xl-4"></div>
    <div class="col-12 col-sm-10 col-md-8 col-lg-6 col-xl-4">

      <div class="card">
        <div class="modal-close" @click="close"><i class="fa-solid fa-xmark"></i></div>
        <div class="card-body">
          <slot></slot>
        </div>

      </div>

    </div>
    <div class="col-0 col-sm-1 col-md-2 col-lg-3 col-xl-4"></div>
  </div>



    </div>
  </div>
</template>

<style scoped>
.modal-window {
  position: fixed;
  z-index: v-bind(zIndex);

  left: 0;
  top: 0;

  background-color: #0000001f;
  height: 100vh;
  width: 100vw;

}

.modal-close{
  position: absolute;
  top: -5px;
  right: 5px;
}

.card{
  min-height: 10vh;
  padding-top: 5px;
}

.modal-inner{
  margin-top: v-bind(marginTop);
}

.fa-xmark:hover{
  cursor: pointer;
  opacity: 0.7;
}
</style>
