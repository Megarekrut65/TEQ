<script setup>
defineProps({
    title: {
        type: String,
        required: true,
    },
    bgColor: {
        type: String,
        default: "primary",
    },
});
</script>

<template>
    <div class="card">
        <div :class="`card-header bg-${bgColor} main-style`">
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
