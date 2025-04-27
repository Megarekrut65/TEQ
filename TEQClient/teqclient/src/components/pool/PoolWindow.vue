<script setup>
import ModalWindow from "@/components/ModalWindow.vue";
import { ref } from "vue";
import { categoryCreateApi, itemCreateApi, poolGetApi } from "@/js/api/pool.js";
import { errorAlert, successAlert } from "@/js/utility/utility.js";
import CategoryTree from "@/components/pool/CategoryTree.vue";
import i18n from "@/i18n/index.js";

const props = defineProps({
  addSelected:{
    type: Function,
    required: true,
  },
  pasteMode:{
    type: Boolean,
    required: true,
  }
})

i18n.useT();

const model = defineModel({ default: false });
const item = defineModel("item");

const pool = ref(null);

poolGetApi()
    .then((res) => {
        pool.value = res;
    })
    .catch(errorAlert);

const createCategory = () => {
  categoryCreateApi({name:i18n.t('newCategory')})
    .then(category => {
      pool.value.categories.push(category);
    })
    .catch(errorAlert);
};

const addToPool = (category) => {
    category.items.push(item.value);

    itemCreateApi(category.id, item.value).catch(errorAlert);
    successAlert(i18n.t('added'));
};

const copyFromPool = (category, categoryItem) => {
  const items = category == null?[categoryItem]: category.items;

  for(let item of items) {
    props.addSelected(item);
  }
  successAlert(i18n.t('added'));
};
</script>

<template>
    <ModalWindow v-model="model" size="medium">
        <template v-slot:header>
            <h3 class="my-0">
                {{ $t("pool") }} <i v-if="pasteMode" class="fa fa-plus btn-hover" @click="createCategory"></i>
            </h3>
        </template>
        <div v-if="pool" class="pool">
            <CategoryTree
                :categories="pool.categories"
                :paste-mode="pasteMode"
                :add-to-pool="addToPool"
                :copy-from-pool="copyFromPool"
            ></CategoryTree>
        </div>
    </ModalWindow>
</template>

<style scoped>
.pool {
    max-height: 60vh;
    overflow-y: auto;
    overflow-x: hidden;
}
</style>
