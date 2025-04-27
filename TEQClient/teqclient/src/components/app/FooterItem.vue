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
                            <img
                                src="@/assets/images/main-logo.png"
                                alt="logo"
                                class="footer-logo"
                            />
                            <p>
                                {{ $t("appDescription") }}
                            </p>
                        </div>
                    </div>
                </div>

                <div class="col-md-2">
                    <div class="footer-menu">
                        <h5>{{ $t("menu") }}</h5>
                        <ul class="menu-list">
                            <li class="menu-item">
                                <a href="#">{{ $t("publicTests") }}</a>
                            </li>
                            <li class="menu-item">
                                <a href="#">{{ $t("savedTests") }}</a>
                            </li>
                            <li class="menu-item">
                                <a href="#">{{ $t("contacts") }}</a>
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="col-md-2">
                    <div class="footer-menu">
                        <h5>{{ $t("account") }}</h5>
                        <ul class="menu-list">
                            <li class="menu-item">
                                <a href="#">{{ $t("createTest") }}</a>
                            </li>
                            <li class="menu-item">
                                <LocalizedLink to="tests/my">{{ $t("myTests") }}</LocalizedLink>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </footer>
</template>

<style scoped></style>
