import { store } from "quasar/wrappers";
import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import SecureLS from "secure-ls";
import menu from "./menu";
import app from "./app";
import products from "./products";
import cart from "./cart";
import login from "./login";
import appinfo from "./appinfo";

const ls = new SecureLS({ isCompression: false });
const persistedState = createPersistedState({
  storage: {
    getItem: (key) => ls.get(key),
    setItem: (key, value) => ls.set(key, value),
    removeItem: (key) => ls.remove(key),
  },
  paths: ["login", "cart"],
});

export default store(function () {
  const Store = createStore({
    modules: {
      login,
      menu,
      app,
      products,
      cart,
      appinfo,
    },

    plugins: [persistedState],
    // enable strict mode (adds overhead!)
    // for dev mode and --debug builds only
    strict: process.env.DEBUGGING,
  });

  return Store;
});
