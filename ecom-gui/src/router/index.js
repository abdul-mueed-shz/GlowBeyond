import { route } from "quasar/wrappers";
import { APP_CONSTANTS } from "src/common/constants/app";
import { APP_ROUTES } from "src/common/constants/_routes";
import { errorNotification } from "src/common/utils/notifications";
import { computed } from "vue";
import {
  createRouter,
  createMemoryHistory,
  createWebHistory,
  createWebHashHistory,
} from "vue-router";
import routes from "./routes";

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

export default route(function ({ store }) {
  const map = computed(() => {
    return store.getters["app/getMAP"];
  });
  const loginDetails = computed(() => {
    return store.getters["login/getLoginDetails"];
  });
  const createHistory = process.env.SERVER
    ? createMemoryHistory
    : process.env.VUE_ROUTER_MODE === "history"
    ? createWebHistory
    : createWebHashHistory;
  const Router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,

    // Leave this as is and make changes in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    history: createHistory(
      process.env.MODE === "ssr" ? void 0 : process.env.VUE_ROUTER_BASE
    ),
  });
  Router.afterEach((to, _) => {
    document.title = `${APP_CONSTANTS.APP_NAME} | ${
      map.value.Link.Routes[to.name] ?? ""
    }`;
  });
  Router.beforeEach((to, from, next) => {
    if (to.meta.requireAuthentication && !loginDetails.value) {
      errorNotification("Unauthenticated");
      next({ path: from.path });
      return;
    }
    next();
  });
  return Router;
});
