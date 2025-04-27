<script setup>
import LocalizedLink from "@/components/l10n/LocalizedLink.vue";
import LanguageSelect from "@/components/l10n/LanguageSelect.vue";
import { ref } from "vue";
import { getUser, logout } from "@/js/utility/auth.js";
import { truncate } from "../../js/utility/utility.js";

const user = ref(getUser());

window.addEventListener("auth", (data) => {
    user.value = data.detail;
    if (!data.detail) {
        window.location.reload();
    }
});
</script>

<template>

  <div class="collapse navbar-collapse main-menu" id="navbarSupportedContent">
    <ul class="navbar-nav mb-2 mb-lg-0 menu-list">
      <li class="nav-item menu-item">
        <LanguageSelect class="nav-link" />
      </li>
      <li class="nav-item">
        <LocalizedLink to="/" class="nav-link">{{ $t("home") }}</LocalizedLink>
      </li>
      <li class="nav-item">
        <LocalizedLink to="/public" class="nav-link">{{ $t("publicTests")  }}</LocalizedLink>
      </li>
      <li class="nav-item">
        <LocalizedLink to="/public" class="nav-link">{{ $t("contacts") }}</LocalizedLink>
      </li>

      <li v-if="user" class="nav-item dropdown dropstart">
        <div class="dropdown">
          <a
            class="dropdown-toggle nav-link pb-2"
            href="#"
            role="button"
            data-bs-toggle="dropdown"
            aria-expanded="false"
            :title="user.fullname"
          >
            <i class="fa-solid fa-user"></i> {{ truncate(user.fullname, 8) }}
          </a>

          <ul class="dropdown-menu">
            <li>
              <a class="dropdown-item" href="#"
              ><i class="fa-regular fa-user"></i> {{ $t("account") }}</a
              >
            </li>
            <li>
              <LocalizedLink class="dropdown-item" to="/editor/new"
              ><i class="fa-solid fa-file-circle-plus"></i>
                {{ $t("createTest") }}
              </LocalizedLink>
            </li>
            <li>
              <LocalizedLink class="dropdown-item" to="/account/tests"
              ><i class="fa-solid fa-newspaper"></i>
                {{ $t("myTests") }}
              </LocalizedLink>
            </li>
            <li>
              <LocalizedLink class="dropdown-item" to="/account/pool"
              ><i class="fa-solid fa-layer-group"></i>
                {{ $t("pool") }}
              </LocalizedLink>
            </li>
            <li>
              <LocalizedLink class="dropdown-item" to="/account/answers"
              ><i class="fa-solid fa-comments"></i>
                {{ $t("myAnswers") }}
              </LocalizedLink>
            </li>
            <li>
              <hr class="dropdown-divider" />
            </li>
            <li>
              <a class="dropdown-item" href="#" @click="logout"
              ><i class="fa-solid fa-arrow-right-from-bracket"></i>
                {{ $t("logout") }}</a
              >
            </li>
          </ul>
        </div>
      </li>
      <li v-else class="nav-item">
        <LocalizedLink to="/auth" class="nav-link">{{ $t("singInUp") }}</LocalizedLink>
      </li>
    </ul>

  </div>
</template>

<style scoped>

.nav-link:hover{
  color: rgb(242, 137, 63);
}
.nav-link{
  padding-bottom: 0;
  font-size: inherit;
  font-family: inherit;
}
.menu-list{
  justify-content: end;
  width: 100%;
}
.dropdown>ul{
  background: rgba(221, 221, 221, 1);
}
</style>
