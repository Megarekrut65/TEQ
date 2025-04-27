<script setup>
import { ref } from "vue";
import { categoryCreateApi, poolGetApi } from "@/js/api/pool.js";
import { errorAlert } from "@/js/utility/utility.js";
import LoadingWindow from "@/components/LoadingWindow.vue";
import LocalizedLink from "@/components/l10n/LocalizedLink.vue";
import i18n from "@/i18n/index.js";
import { useRouter } from "vue-router";

const pool = ref(null);

const loading = ref(true);

poolGetApi()
    .then((res) => {
        pool.value = res;
    })
    .catch(errorAlert)
    .finally(() => {
        loading.value = false;
    });

i18n.useT();
const router = useRouter();

const createCategory = () => {
    categoryCreateApi({ name: i18n.t("category") })
        .then((res) => {
            router.push({ name: "category", params: { categoryId: res.id } });
        })
        .catch(errorAlert);
};
</script>

<template>
    <LoadingWindow v-if="loading" />
    <div v-if="pool">
        <div class="container">
            <div class="row mb-4">
                <div class="col">
                    <h2>
                        {{ $t("pool") }}
                        <a href="#" @click="createCategory"><i class="fa fa-plus"></i></a>
                    </h2>
                </div>
            </div>

            <div class="row">
                <div class="col-12" v-if="pool?.categories?.length === 0">
                    <p>
                        {{ $t("missingCategory") }}.
                        <a href="#" @click="createCategory">{{ $t("create") }}?</a>
                    </p>
                </div>

                <div
                    class="col-12 col-sm-6 col-md-4 col-lg-3 mt-2"
                    v-for="category in pool.categories"
                    :key="category"
                >
                    <div class="card">
                        <div class="card-body d-flex justify-content-between">
                            <LocalizedLink :to="`category/${category.id}`">{{
                                category.name
                            }}</LocalizedLink>
                            <LocalizedLink :to="`category/${category.id}`"
                                ><i class="fa-solid fa-arrow-right"></i
                            ></LocalizedLink>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>
