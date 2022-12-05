import { boot } from "quasar/wrappers";
import { APP_CONSTANTS, COUPLED_APPS } from "src/common/constants/app";

let $router = null;
let $store = null;

export default boot(async ({ store, app, router }) => {
  $router = router;
  $store = store;
  setGlobalProperties(app);
});

function setGlobalProperties(app) {
  app.config.globalProperties.$appName = APP_CONSTANTS.APP_NAME;
  setLoginAppURL(app);
}
function setLoginAppURL(app) {
  const loginApp = COUPLED_APPS.find((app) => app.app_name.includes("login"));
  if (!loginApp) {
    return;
  }
  if (process.env.DEV) {
    app.config.globalProperties.$loginAppUrl = loginApp.url.local;
  } else if (process.env.PROD) {
    app.config.globalProperties.$loginAppUrl = loginApp.url.prod;
  }
}
export function useGlobalRouter() {
  return $router;
}
export function useGlobalStore() {
  return $store;
}
