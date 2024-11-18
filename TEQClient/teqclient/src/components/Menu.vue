<script setup>
import LocalizedLink from "@/components/l10n/LocalizedLink.vue";
import LanguageSelect from "@/components/l10n/LanguageSelect.vue";
</script>

<template>
  <nav id="navbar">
    <div class="main-menu stellarnav">
      <ul class="menu-list">
        <li class="menu-item">
          <LanguageSelect />
        </li>
        <li class="menu-item active"><a href="#home">Home</a></li>
        <li class="menu-item"><a href="#featured-books" class="nav-link">Featured</a></li>
        <li class="menu-item"><a href="#popular-books" class="nav-link">Popular</a></li>
        <li class="menu-item"><a href="#special-offer" class="nav-link">Offer</a></li>
        <li class="menu-item"><a href="#latest-blog" class="nav-link">Articles</a></li>
        <li class="menu-item">
          <LocalizedLink to="/auth" class="nav-link">Sign in/up</LocalizedLink>
        </li>

      </ul>
    </div>
  </nav>
</template>

<style scoped></style>
