<script setup>
import LocalizedLink from "@/components/l10n/LocalizedLink.vue";
import LanguageSelect from "@/components/l10n/LanguageSelect.vue";
import { ref } from "vue";
import { getUser, logout } from "@/js/utility/auth.js";

const user = ref(getUser());

window.addEventListener("auth", (data) => {
  user.value = data.detail;
});
</script>

<template>
  <nav id="navbar">
    <div class="main-menu stellarnav">
      <ul class="menu-list">
        <li class="menu-item">
          <LanguageSelect />
        </li>
        <li class="menu-item active">
          <LocalizedLink to="/">{{ $t("home") }}</LocalizedLink>
        </li>
        <li class="menu-item"><a href="#featured-books" class="nav-link">{{ $t("publicTests") }}</a></li>
        <li class="menu-item"><a href="#popular-books" class="nav-link">{{ $t("savedTests") }}</a></li>
        <li class="menu-item"><a href="#special-offer" class="nav-link">{{ $t("contacts") }}</a></li>
        <li v-if="user" class="nav-item dropdown">
          <div class="dropdown">
            <a class="dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
               aria-expanded="false">
              <i class="fa-solid fa-user"></i> {{ user.email }}
            </a>

            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#"><i class="fa-regular fa-user"></i> {{ $t("account") }}</a></li>
              <li>
                <LocalizedLink class="dropdown-item" to="/editor/new"><i class="fa-solid fa-file-circle-plus"></i>
                  {{ $t("createTest") }}
                </LocalizedLink>
              </li>
              <li>
                <LocalizedLink class="dropdown-item" to="/tests/my"><i class="fa-solid fa-newspaper"></i>
                  {{ $t("myTests") }}
                </LocalizedLink>
              </li>
              <li>
                <hr class="dropdown-divider">
              </li>
              <li><a class="dropdown-item" href="#" @click="logout"><i class="fa-solid fa-arrow-right-from-bracket"></i>
                {{ $t("logout") }}</a></li>
            </ul>
          </div>
        </li>
        <li v-else class="menu-item">
          <LocalizedLink to="/auth" class="nav-link">{{ $t("singInUp") }}</LocalizedLink>
        </li>

      </ul>
    </div>
  </nav>
</template>

<style scoped></style>
