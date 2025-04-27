<script setup>

import { categoryUpdateApi, itemCreateApi, itemDeleteApi, itemUpdateApi } from "@/js/api/pool.js";
import TestItem from "@/components/test/TestItem.vue";
import FormWrapper from "@/components/FormWrapper.vue";
import { ref } from "vue";
import { defaultAnswer } from "@/js/data-types.js";
import { errorAlert } from "@/js/utility/utility.js";
import PoolWindow from "@/components/pool/PoolWindow.vue";

const props = defineProps({
  instance: {
    type: Object,
    required: true
  }
});

const formData = ref(props.instance);

const addNewAnswer = () => {
  itemCreateApi(formData.value.id, defaultAnswer(formData.value.id))
    .then((res) => {
      formData.value.items.push(res);
    })
    .catch(errorAlert);
};

const onItemPaste = (data)=>{
  itemCreateApi(data)
    .then((res) => {
      formData.value.items.push(res);
    })
    .catch(errorAlert);
};

const updateCategory = () => {
  if(formData.value.name === "") return;

  categoryUpdateApi(formData.value.id, formData.value).catch(errorAlert);
};

const onItemRemoved = (index) => {
  if (index < 0 || index >= formData.value.items.length) return;

  formData.value.items.splice(index, 1);
  itemDeleteApi(formData.value.id, index).catch(errorAlert);
};

const poolItem = ref(null);
const poolActive = ref(false);
const onOpenPool = (item)=>{
  poolActive.value = true;
  poolItem.value = item;
};
</script>

<template>
  <PoolWindow v-model="poolActive" v-model:item="poolItem"></PoolWindow>

  <FormWrapper :title="formData.title" show-menu>
    <template v-slot:menu>
      <a class="dropdown-item" href="#">
        {{ $t("delete") }}
      </a>
    </template>
    <form @change="updateCategory">
      <div>
        <label class="form-label" for="title">{{ $t("name") }}</label>
        <input
          v-model.trim="formData.name"
          type="text"
          class="form-control"
          maxlength="100"
          required
        />
      </div>
    </form>
  </FormWrapper>

  <div>
    <div class="mt-3">
      <TestItem
        v-for="(item, index) in formData.items"
        :key="index"
        :index="index + 1"
        v-model="formData.items[index]"
        :on-item-removed="() => onItemRemoved(index)"
        :test-id="formData.id"
        auto-check
        :update-api="itemUpdateApi"
        :on-item-paste="onItemPaste"
        :open-pool="onOpenPool"
      />
    </div>
    <div class="d-flex justify-content-center">
      <img src="@/assets/images/plus.png" class="btn-img" alt="plus" @click="addNewAnswer" />
    </div>
  </div>
</template>

<style scoped>

</style>
