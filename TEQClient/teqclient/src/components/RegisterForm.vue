<script setup>
import FormWrapper from "@/components/FormWrapper.vue";

const onSubmit = () => {};
</script>

<template>
    <FormWrapper title="Register">
        <form @submit.prevent="onSubmit">
            <div class="form-group">
                <label for="title">{{$t('fullname')}}</label>
                <input
                    v-model.trim="formData.title"
                    type="text"
                    class="form-control"
                    placeholder="Enter title"
                    maxlength="255"
                    required
                />
            </div>
        </form>
    </FormWrapper>
</template>

<style scoped></style>
