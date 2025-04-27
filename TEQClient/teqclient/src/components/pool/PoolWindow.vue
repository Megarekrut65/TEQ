<script setup>
import ModalWindow from "@/components/ModalWindow.vue";
import { ref, watch } from "vue";
import { itemCreateApi, poolGetApi } from "@/js/api/pool.js";
import { errorAlert } from "@/js/utility/utility.js";
import CategoryTree from "@/components/pool/CategoryTree.vue";

const model = defineModel({ default: false });
const item = defineModel("item");
const pasteMode = defineModel("pasteMode", { type: Boolean });

const pool = ref(null);

poolGetApi()
    .then((res) => {
        pool.value = res;
    })
    .catch(errorAlert);

const createCategory = () => {};

const addToPool = (category) => {
    itemCreateApi(category.id, item.value).catch(errorAlert);
};

const copyFromPool = (category, categoryItem) => {};
</script>

<template>
    <ModalWindow v-model="model" size="medium">
        <template v-slot:header>
            <h3 class="my-0">
                {{ $t("pool") }} <a href="#" @click="createCategory"><i class="fa fa-plus"></i></a>
            </h3>
        </template>
        <div v-if="pool" class="pool">
            <CategoryTree
                :categories="pool.categories"
                :paste-mode="pasteMode"
                :add-to-pool="addToPool"
                copy-from-pool="copyFromPool"
            ></CategoryTree>
        </div>
    </ModalWindow>
</template>

<style scoped>
.pool {
    max-height: 60vh;
    overflow-y: auto;
}
</style>
