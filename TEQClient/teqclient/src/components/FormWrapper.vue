<script setup>
defineProps({
    title: {
        type: String,
        required: false
    },
    bgColor: {
        type: String,
        default: "secondary",
    },
});
</script>

<template>
    <div class="card">
        <div v-if="title" :class="`card-header bg-${bgColor}`">
            <h4 class="form-title">{{ title }}</h4>
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
</style>
