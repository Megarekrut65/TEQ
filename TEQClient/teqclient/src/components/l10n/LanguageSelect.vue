<script setup>
import { ref } from "vue";
import i18n, { supportedLocales } from "@/i18n";
import { useRoute } from "vue-router";
import router from "@/router";


const locales = ref(supportedLocales);
const locale = ref(supportedLocales[i18n.getLocale()]);
const onUpdated = ref(i18n.vueI18n);

const route = useRoute();

const onLanguageChanged = (language) => {
  if (language === i18n.getLocale()) return;
  const path = route.path.replace(`/${i18n.getLocale()}`, `/${language}`);
  i18n.setLocale(language);

  router.push(path);
};
const updateLocale = () => {
  locale.value = supportedLocales[i18n.getLocale()];
};

</script>
<template>
  <div class="dropdown">
    <a class="dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
      <i :class="`${locale.flag} flag-icon m-0`" v-bind="updateLocale()"></i>
    </a>

    <ul class="dropdown-menu">
      <li>
        <a class="dropdown-item menu-row" href="#">
          <div><i :class="`${locale.flag} flag-icon`"></i></div>
          <div class="item-margin">{{ locale.name }}</div>
          <div><i class="fa fa-check text-success"></i></div>
        </a>
      </li>

      <li>
        <hr class="dropdown-divider">
      </li>
      <li v-for="(data, index) in locales" :key="index" @click="onLanguageChanged(index)">
        <a class="dropdown-item" href="#">
          <i
            :class="`${data.flag} flag-icon`"></i>
          {{ data.name }}
        </a>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.menu-row {
  display: flex;
  justify-content: space-between;
}

.item-margin {
  margin-left: 5px;
  margin-right: 5px;
}

.dropdown-toggle:hover {
  opacity: 0.5;
}
</style>
