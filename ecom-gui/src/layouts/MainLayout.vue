<!-- TODO: MAKE STORES PERSISTENT -->
<!-- TODO: IMPROVE UI -->
<!-- TODO: REPLACE CONSOLE LOGS WITH SHOWERROR OR SHOWSUCCESS UTIL FUNCTION CALLS -->
<!-- TODO: MAKE UTIL FUNCTIONS FOR CART ITEM DECREMENT INCREMENT AND REMOVAL IN CART ITEMS COMPONENT -->

<template>
  <q-layout view="lHh LpR lff">
    <q-header>
      <div class="bg-notif-message q-py-sm flex flex-center text-weight-medium">
        <span>Free shipping above order 300 Dhs</span>
        <span>
          <q-icon
            name="mdi-arrow-right"
            flat
            class="cursor-pointer q-px-xs"
            size="sm"
          ></q-icon>
        </span>
      </div>
      <q-toolbar class="bg-white text-secondary q-px-xl">
        <q-btn
          flat
          dense
          round
          icon="mdi-menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />
        <q-space></q-space>
        <div>
          <q-img
            class="cursor-pointer"
            @click="() => $router.push(APP_ROUTES.HOME.PATH)"
            src="../assets/LOGO.png"
            width="200px"
          ></q-img>
        </div>
        <q-space></q-space>
        <q-btn
          v-if="!toggleSearch"
          flat
          @click="() => (toggleSearch = !toggleSearch)"
          icon="mdi-magnify"
          round
        ></q-btn>
        <q-input
          v-else
          class="bg-white rounded-borders"
          dense
          :placeholder="!search && 'Search'"
          v-model="search"
          @update:model-value="searchProducts"
          debounce="1000"
          clearable
        >
          <template #prepend>
            <q-icon
              class="cursor-pointer"
              @click="searchProducts"
              name="mdi-magnify"
            ></q-icon>
          </template>
          <template #append>
            <q-icon
              class="cursor-pointer"
              @click="() => (toggleSearch = !toggleSearch)"
              name="mdi-close"
            >
              <q-tooltip> Close search </q-tooltip></q-icon
            >
          </template>
        </q-input>
        <AuthMenu />
      </q-toolbar>
    </q-header>
    <q-drawer
      v-model="leftDrawerOpen"
      :width="250"
      :bordered="$route.name != APP_ROUTES.HOME.NAME"
    >
      <div class="q-pt-md">
        <main-menu
          v-for="item in menuList"
          :key="item.name"
          :item="item"
          :mini-state="miniState"
        />
      </div>
    </q-drawer>
    <q-page-container>
      <q-ajax-bar ref="bar" position="bottom" color="accent" size="10px" />
      <router-view :key="$route.fullPath" />
    </q-page-container>
  </q-layout>
</template>

<script>
import MainMenu from "src/components/MainMenu.vue";
import AuthMenu from "src/components/AuthenticationMenu.vue";
import { APP_ROUTES } from "../common/constants/_routes";
import { computed, getCurrentInstance, onMounted, ref } from "vue";
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";

export default {
  components: {
    MainMenu,
    AuthMenu,
  },
  setup() {
    // CONSTANTS
    const toggleSearch = ref(false);
    const app = getCurrentInstance();

    const search = ref("");

    const store = useStore();

    const router = useRouter();

    const route = useRoute();

    const leftDrawerOpen = ref(false);

    // COMPUTED PROPERTIES

    const MAP = computed(() => {
      return store.getters["app/getMAP"];
    });

    const selectedMenuItem = computed(() => {
      return store.getters["menu/getSelectedMenuItem"];
    });

    const miniState = computed(() => {
      return store.getters["app/getMiniState"];
    });

    const menuList = computed(() => {
      return store.getters["menu/getMenuList"];
    });

    const loginDetails = computed(() => {
      return store.getters["login/getLoginDetails"];
    });

    // FUNCTIONS
    function toggleLeftDrawer() {
      leftDrawerOpen.value = !leftDrawerOpen.value;
    }

    function searchProducts(query) {
      if (!query) {
        router.push({ name: APP_ROUTES.HOME.NAME });
        return;
      }
      store.dispatch("products/search", { query }).then((res) => {
        if (res.length > 0) {
          router.push({ name: APP_ROUTES.SEARCH_RESULTS.NAME });
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
        store.dispatch("login/setLoginDetails", null);
        clearInterval(intervalId);
        store.dispatch("login/setIntervalId", null);
        return;
      }
      const intervalId = setInterval(() => {
        if (!isTokenValid()) {
          store.dispatch("login/setLoginDetails", null);
          clearInterval(intervalId);
          store.dispatch("login/setIntervalId", null);
        }
      }, 60000);
      store.dispatch("login/setIntervalId", intervalId);
    }
    onMounted(async () => {
      // headers: {
      //   AUTHTOKEN: loginDetails.value.auth_token, //the token is a variable which holds the token
      // }
      store.dispatch("menu/setSelectedMenuItem", route.name);
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
          await store.dispatch("login/getAuthDetails", queryObject);
          setTokenWatcher();
          window.history.replaceState({}, "home", window.location.origin);
        }
      }
    });

    return {
      toggleSearch,
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
