import { APP_ROUTES } from "../common/constants/_routes";
const routes = [
  {
    path: APP_ROUTES.BASE.PATH,
    component: () => import("layouts/BlankLayout.vue"),
    children: [
      {
        path: "",
        name: APP_ROUTES.BASE.NAME,
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
        path: APP_ROUTES.SUMMER.PATH,
        name: APP_ROUTES.SUMMER.NAME,
        meta: {},
        component: () => import("pages/SummerCollection.vue"),
      },
    ],
  },
  {
    path: APP_ROUTES.BASE.PATH,
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: APP_ROUTES.WINTER.PATH,
        name: APP_ROUTES.WINTER.NAME,
        meta: {},
        component: () => import("pages/WinterCollection.vue"),
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

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
