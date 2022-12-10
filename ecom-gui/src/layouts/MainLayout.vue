<!-- TODO: MAKE STORES PERSISTENT -->
<!-- TODO: IMPROVE UI -->
<!-- TODO: REPLACE CONSOLE LOGS WITH SHOWERROR OR SHOWSUCCESS UTIL FUNCTION CALLS -->
<!-- TODO: MAKE UTIL FUNCTIONS FOR CART ITEM DECREMENT INCREMENT AND REMOVAL IN CART ITEMS COMPONENT -->

<template>
  <q-layout view="hHh Lpr lFf">
    <q-header :elevated="$route.name != APP_ROUTES.HOME.NAME">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="mdi-menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />
        <q-toolbar-title>
          {{ MAP.APPNAME }}
        </q-toolbar-title>
        <q-input
          class="bg-white rounded-borders q-my-sm"
          dense
          filled
          label="Search"
          v-model="search"
          @update:model-value="searchProducts"
          debounce="500"
        >
          <template #append>
            <q-btn flat @click="searchProducts" icon="mdi-magnify"></q-btn>
          </template>
        </q-input>
        <AuthMenu />
      </q-toolbar>
    </q-header>
    <q-drawer
      v-model="leftDrawerOpen"
      :mini="miniState"
      :breakpoint="10"
      :width="250"
      show-if-above
      :bordered="$route.name != APP_ROUTES.HOME.NAME"
      class="bg-primary text-white"
    >
      <main-menu
        v-for="item in menuList"
        :key="item.name"
        :item="item"
        :mini-state="miniState"
      />
    </q-drawer>
    <q-page-container>
      <q-ajax-bar ref="bar" position="bottom" color="accent" size="10px" />
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import MainMenu from "src/components/MainMenu.vue";
import AuthMenu from "src/components/AuthenticationMenu.vue";
import { APP_ROUTES } from "../common/constants/_routes";
import { computed, getCurrentInstance, onMounted, ref } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

export default {
  components: {
    MainMenu,
    AuthMenu,
  },
  setup() {
    // CONSTANTS
    const app = getCurrentInstance();

    const search = ref("");

    const $store = useStore();

    const $router = useRouter();

    const leftDrawerOpen = ref(false);

    // COMPUTED PROPERTIES

    const MAP = computed(() => {
      return $store.getters["app/getMAP"];
    });

    const selectedMenuItem = computed(() => {
      return $store.getters["menu/getSelectedMenuItem"];
    });

    const miniState = computed(() => {
      return $store.getters["app/getMiniState"];
    });

    const menuList = computed(() => {
      return $store.getters["menu/getMenuList"];
    });

    const loginDetails = computed(() => {
      return $store.getters["login/getLoginDetails"];
    });

    // FUNCTIONS
    function toggleLeftDrawer() {
      $store.commit("app/toggleMiniState");
    }

    function searchProducts(query) {
      $store.dispatch("products/search", { query }).then((res) => {
        if (res.length > 0) {
          $router.push(APP_ROUTES.SEARCH_RESULTS.NAME);
        }
      });
    }

    function isTokenValid() {
      const currentDate = new Date();
      const expiryDate = new Date();
      const currentTime = ~~(currentDate.getTime() / 1000);
      expiryDate.setSeconds(loginDetails.value.token_exp_date - currentTime);
      return expiryDate > currentDate;
    }
    function setTokenWatcher() {
      if (!isTokenValid()) {
        $store.dispatch("login/setLoginDetails", null);
        clearInterval(intervalId);
        $store.dispatch("login/setIntervalId", null);
        return;
      }
      const intervalId = setInterval(() => {
        if (!isTokenValid()) {
          $store.dispatch("login/setLoginDetails", null);
          clearInterval(intervalId);
          $store.dispatch("login/setIntervalId", null);
        }
      }, 60000);
      $store.dispatch("login/setIntervalId", intervalId);
    }
    onMounted(async () => {
      // headers: {
      //   AUTHTOKEN: loginDetails.value.auth_token, //the token is a variable which holds the token
      // }
      if (loginDetails.value) {
        setTokenWatcher();
        return;
      }
      if (
        app.appContext.config.globalProperties.$loginAppUrl ===
        document.referrer
      ) {
        let querySearch = window.location.search.substring(1);
        const queryObject = Object.fromEntries(
          new URLSearchParams(querySearch)
        );
        if (queryObject.auth_token) {
          await $store.dispatch("login/getAuthDetails", queryObject);
          setTokenWatcher();
          window.history.replaceState({}, "home", window.location.origin);
        }
      }
    });

    return {
      leftDrawerOpen,
      MAP,
      selectedMenuItem,
      miniState,
      menuList,
      APP_ROUTES,
      toggleLeftDrawer,
      search,
      searchProducts,
    };
  },
};
</script>
