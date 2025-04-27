<script setup>
import DotsMenu from "@/components/DotsMenu.vue";

defineProps({
    title: {
        type: String,
        required: false,
    },
    bgColor: {
        type: String,
        default: "secondary",
    },
    showMenu: {
        type: Boolean,
        required: false,
        default: false,
    },
});
</script>

<template>
    <div class="card">
        <div v-if="title" :class="`card-header bg-${bgColor}`">
            <h4 class="form-title">{{ title }}</h4>
            <div v-if="showMenu">
                <DotsMenu>
                    <slot name="menu"></slot>
                </DotsMenu>
            </div>
        </div>
        <div class="card-body">
            <slot></slot>
        </div>
    </div>
</template>
<style scoped>
h4 {
    vertical-align: middle;
}
.card-header {
    display: flex;
    justify-content: space-between;
}
</style>
