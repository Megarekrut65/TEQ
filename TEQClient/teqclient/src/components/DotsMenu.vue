<template>
  <div class="btn-group dropstart">
    <button
      type="button"
      class="btn-none"
      data-bs-toggle="dropdown"
      aria-haspopup="true"
      aria-expanded="false"
    >
      <i class="fa-solid fa-ellipsis-vertical dots-btn text-dark"></i>
    </button>
    <ul class="dropdown-menu" role="menu">
      <slot></slot>
    </ul>
  </div>
</template>
<style scoped>
.btn-none{
  border: none;
  background: none;
  margin: 0;
}
.dropdown-menu{
  border: 1px solid black;
  border-radius: 5px;
}
</style>

