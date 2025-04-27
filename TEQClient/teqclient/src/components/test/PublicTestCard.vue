<script setup>
import { truncate } from "../../js/utility/utility.js";

defineProps({
  test:{
    type: Object,
    required: true
  }
})
</script>

<template>
  <div class="col-12 col-md-6 col-lg-4 mt-3">
    <div class="card">
      <div class="card-header">
        <div>{{test.title}}</div> <div class="badge bg-secondary" :title="$t('answerCount')">{{test.answerCount}}</div>
      </div>
      <div class="card-body">
        <span v-if="test.description">
          {{truncate(test.description, 100)}}
        </span>
      </div>
      <div class="card-footer">
        <RouterLink :to="{name:'pass', params:{testId:test.id}}">{{$t('pass')}}</RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped>
.badge{
  position: absolute;
  top: 5px;
  right: 5px;
}
.card{
  height: 100%;
}
</style>
