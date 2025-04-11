<script setup>
import { MULTIPLE, SINGLE, TEXT } from "@/js/types.js";

defineProps({
  index:{
    type: Number,
    required: true
  },
  readonly:{
    type: Boolean,
    required: false,
    default: false
  },
  item:{
    type: Object,
    required: true
  }
});

const formData = defineModel({required:true});

</script>

<template>
  <div class="card mt-3">
    <div class="card-body">
    <label>{{index}}. {{ item.text }}</label>

    <div v-if="item.type === SINGLE || item.type === MULTIPLE" class="mb-3">
      <label class="form-label">{{ $t("choices") }}</label>

      <div v-for="(choice, i) in item.choices" :key="choice">
        <div class="form-check">
          <input v-if="item.type === SINGLE" class="form-check-input" type="radio"
                 :name="`radio_${index}`" v-model="formData.choices[0]" :value="i"
                 :disabled="readonly">

          <input v-else class="form-check-input" type="checkbox" v-model="formData.choices" :value="i"
                 :disabled="readonly">

          <label class="form-check-label" >{{choice.text}}</label>
        </div>
      </div>
      <input class="form-check-input hide" type="radio"
             :name="`radio_${index}`" checked>
    </div>

    <div v-if="item.type === TEXT" class="mb-3">
        <textarea
          v-model="formData.answer"
          class="form-control"
          rows="3"
          :readonly="readonly"
        ></textarea>
    </div>
      </div>
  </div>
</template>

<style scoped>
button {
  margin: 0;
}

form {
  margin-bottom: 0;
}

.hide{
  display: none;
}

</style>
