import { createRouter, createWebHistory } from "vue-router";
import i18n, { defaultLocale } from "@/i18n";
import { ifAuthenticated } from "@/js/utility/auth.js";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      redirect: `/${defaultLocale}`,
    },
    {
      path: "/:locale",
      children: [
        {
          path: "",
          name: "home",
          component: () => import("../views/HomeView.vue"),
        },
        {
          path: "public",
          name: "public",
          component: () => import("../views/PublicTestsView.vue"),
        },
        {
          path: "contacts",
          name: "contacts",
          component: () => import("../views/ContactsView.vue"),
        },
        {
          path: "privacy",
          name: "privacy",
          component: () => import("../views/PrivacyView.vue"),
        },
        {
          path: "auth",
          name: "auth",
          component: () => import("../views/AuthView.vue"),
        },
        {
          path: "account",
          name: "account",
          component: () => import("../views/AccountView.vue"),
          beforeEnter: ifAuthenticated,
        },
        {
          path: "account/tips",
          name: "tips",
          component: () => import("../views/TipsView.vue"),
          beforeEnter: ifAuthenticated,
        },
        {
          path: "editor/:testId",
          name: "editor",
          component: () => import("../views/TestEditorView.vue"),
          beforeEnter: ifAuthenticated,
        },
        {
          path: "pass/:testId",
          name: "pass",
          component: () => import("../views/TestPassView.vue"),
          beforeEnter: ifAuthenticated,
        },
        {
          path: "view/:testId",
          name: "view",
          component: () => import("../views/LastAnswerView.vue"),
          beforeEnter: ifAuthenticated,
        },
        {
          path: "category/:categoryId",
          name: "category",
          component: () => import("../views/CategoryView.vue"),
          beforeEnter: ifAuthenticated,
        },
        {
          path: "account/pool",
          name: "pool",
          component: () => import("../views/PoolView.vue"),
          beforeEnter: ifAuthenticated,
        },
        {
          path: "account/tools",
          name: "tools",
          component: () => import("../views/ToolsView.vue"),
          beforeEnter: ifAuthenticated,
        },
        {
          path: "answer/:answerId",
          name: "answer",
          component: () => import("../views/AnswerView.vue"),
          beforeEnter: ifAuthenticated,
        },
        {
          path: "editor/new",
          name: "new-editor",
          component: () => import("../views/NewTestEditorView.vue"),
          beforeEnter: ifAuthenticated,
        },
        {
          path: "account/tests",
          name: "my-tests",
          component: () => import("../views/MyTestsView.vue"),
          beforeEnter: ifAuthenticated,
        },
        {
          path: "account/answers",
          name: "my-answers",
          component: () => import("../views/MyAnswersView.vue"),
          beforeEnter: ifAuthenticated,
        },
      ],
    },
    {
      path: "/:pathMatch(.*)*",
      name: "not-found",
      component: () => import("../views/NotFoundView.vue"),
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to === from) return savedPosition;

    return { top: 0 };
  },
});

router.beforeEach((to, from) => {
  const newLocale = to.params.locale;
  const prevLocale = from.params.locale;

  if (newLocale === prevLocale) {
    return;
  }
  i18n.setLocale(newLocale);
});

export default router;
