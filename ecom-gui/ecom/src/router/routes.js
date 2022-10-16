const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/HomePage.vue") }],
  },
  {
    path: "/login",
    component: () => import("layouts/BlankLayout.vue"),
    children: [{ path: "", component: () => import("pages/LoginPage.vue") }],
  },
  {
    path: "/summer",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/SummerCollection.vue") },
    ],
  },
  {
    path: "/winter",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/WinterCollection.vue") },
    ],
  },
  {
    path: "/cart",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/CartPage.vue") }],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
