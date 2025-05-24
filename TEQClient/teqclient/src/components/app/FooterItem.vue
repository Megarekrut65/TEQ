<script setup>
import LocalizedLink from "@/components/l10n/LocalizedLink.vue";
</script>

<template>
  <footer id="footer">
    <div class="container">
      <div class="row">
        <div class="col-md-8">
          <div class="footer-item">
            <div class="company-brand">
              <img src="@/assets/images/main-logo.png" alt="logo" class="footer-logo" />
              <p>{{ $t("appName") }} — {{ $t("aboutApp") }}</p>
            </div>
          </div>
        </div>

        <div class="col-md-2">
          <div class="footer-menu">
            <h5>{{ $t("menu") }}</h5>
            <ul class="menu-list">
              <li class="menu-item">
                <LocalizedLink to="/">{{ $t("home") }}</LocalizedLink>
              </li>
              <li class="menu-item">
                <LocalizedLink to="/public">{{ $t("publicTests") }}</LocalizedLink>
              </li>

              <li class="menu-item">
                <LocalizedLink to="/contacts">{{ $t("contacts") }}</LocalizedLink>
              </li>
              <li class="menu-item">
                <LocalizedLink to="/privacy">{{ $t("privacy.title") }}</LocalizedLink>
              </li>
            </ul>
          </div>
        </div>

        <div class="col-md-2">
          <div class="footer-menu">
            <h5>{{ $t("account") }}</h5>
            <ul class="menu-list">
              <li class="menu-item">
                <LocalizedLink to="/account/tests">{{ $t("myTests") }}</LocalizedLink>
              </li>
              <li class="menu-item">
                <LocalizedLink to="/account/answers">{{ $t("answers") }}</LocalizedLink>
              </li>
              <li class="menu-item">
                <LocalizedLink to="/account/tools">{{ $t("tools") }}</LocalizedLink>
              </li>
              <li class="menu-item">
                <LocalizedLink to="/account/tips">{{ $t("tips") }}</LocalizedLink>
              </li>
              <li class="menu-item">
                <LocalizedLink to="/account/pool">{{ $t("pool") }}</LocalizedLink>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped></style>
