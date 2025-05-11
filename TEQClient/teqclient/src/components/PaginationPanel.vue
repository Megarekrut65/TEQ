<template>
  <nav v-if="totalPages !== 1">
    <ul class="pagination">
      <li class="page-item" :class="{ disabled: !hasPrevious }">
        <div class="page-link pagination-color" @click.prevent="goToPage(currentPage - 1)">
          {{ $t("prev") }}
        </div>
      </li>

      <template v-if="hasPrevious && currentPage - 1 !== 1">
        <li class="page-item">
          <div class="page-link pagination-color" @click.prevent="goToPage(1)">1</div>
        </li>
        <li class="page-item disabled">
          <a class="page-link pagination-color" href="#">...</a>
        </li>
      </template>

      <li v-if="hasPrevious" class="page-item">
        <div class="page-link pagination-color" @click.prevent="goToPage(currentPage - 1)">
          {{ currentPage - 1 }}
        </div>
      </li>

      <li class="page-item active">
        <div class="page-link pagination-color">{{ currentPage }}</div>
      </li>

      <li v-if="hasNext" class="page-item">
        <div class="page-link pagination-color" @click.prevent="goToPage(currentPage + 1)">
          {{ currentPage + 1 }}
        </div>
      </li>

      <template v-if="hasNext && currentPage + 1 !== totalPages">
        <li class="page-item disabled">
          <a class="page-link pagination-color" href="#">...</a>
        </li>
        <li class="page-item">
          <div class="page-link pagination-color" @click.prevent="goToPage(totalPages)">
            {{ totalPages }}
          </div>
        </li>
      </template>

      <li class="page-item" :class="{ disabled: !hasNext }">
        <div class="page-link pagination-color" @click.prevent="goToPage(currentPage + 1)">
          {{ $t("next") }}
        </div>
      </li>
    </ul>
  </nav>
</template>

<script setup>
import { computed, defineProps } from "vue";

const props = defineProps({
  currentPage: { type: Number, required: true },
  totalPages: { type: Number, required: true },
  onPageChange: { type: Function, required: true },
});

const hasPrevious = computed(() => props.currentPage > 1);
const hasNext = computed(() => props.currentPage < props.totalPages);

function goToPage(page) {
  if (page >= 1 && page <= props.totalPages && page !== props.currentPage) {
    props.onPageChange(page);
  }
}
</script>
<style scoped>
.pagination-color {
  background-color: #faf4d0;
  border: 1px solid rgb(241, 170, 120);
}
.pagination-color:hover {
  color: white;
  cursor: pointer;
}
.pagination .disabled .page-link {
  pointer-events: none;
  opacity: 0.6;
  background-color: #e9ecef;
  color: #6c757d;
}
.pagination .active .page-link {
  background-color: rgb(242, 137, 63);
}
</style>
