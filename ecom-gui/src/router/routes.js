import { APP_ROUTES } from "../common/constants/_routes";
const routes = [
  {
    path: APP_ROUTES.BASE.PATH,
    component: () => import("layouts/BlankLayout.vue"),
    children: [
      {
        path: "",
        name: APP_ROUTES.BASE.NAME,
        beforeEnter: (to, from, next) => {
          next(APP_ROUTES.HOME.PATH);
        },
        meta: {},
        component: () => import("pages/LoginPage.vue"),
      },
    ],
  },
  {
    path: APP_ROUTES.BASE.PATH,
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: APP_ROUTES.HOME.PATH,
        name: APP_ROUTES.HOME.NAME,
        meta: {},
        component: () => import("pages/HomePage.vue"),
      },
    ],
  },
  {
    path: APP_ROUTES.BASE.PATH,
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: APP_ROUTES.CATEGORY.PATH + "/:slug",
        name: APP_ROUTES.CATEGORY.NAME,
        meta: {},
        component: () => import("pages/CategoryPage.vue"),
      },
    ],
  },
  {
    path: APP_ROUTES.BASE.PATH,
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: APP_ROUTES.CART.PATH,
        name: APP_ROUTES.CART.NAME,
        meta: {},
        component: () => import("pages/CartPage.vue"),
      },
    ],
  },
  {
    path: APP_ROUTES.BASE.PATH,
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: APP_ROUTES.PRODUCT_DETAILS.PATH,
        name: APP_ROUTES.PRODUCT_DETAILS.NAME,
        meta: {},
        component: () => import("pages/ProductDetails.vue"),
      },
    ],
  },
  {
    path: APP_ROUTES.BASE.PATH,
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: APP_ROUTES.SEARCH_RESULTS.PATH,
        name: APP_ROUTES.SEARCH_RESULTS.NAME,
        meta: {},
        component: () => import("pages/SearchResults.vue"),
      },
    ],
  },
  {
    path: APP_ROUTES.BASE.PATH,
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: APP_ROUTES.ACCOUNT_DETAILS.PATH,
        name: APP_ROUTES.ACCOUNT_DETAILS.NAME,
        meta: {
          requireAuthentication: true,
        },
        component: () => import("pages/AccountDetails.vue"),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
