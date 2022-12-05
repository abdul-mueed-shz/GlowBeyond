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
        <q-btn
          outline
          class="q-ml-sm"
          label="login"
          @click="redirectToLogin"
        ></q-btn>
        <!-- <div class="q-pl-md" id="logDetails">
          <q-btn outline icon="mdi-account" color="" :label="MAP.LOGIN">
            <q-menu fit>
              <q-card
                style="min-width: 280px"
                flat
                class="column text-primary flex-center q-mt-md"
              >
                <q-card-section
                  class="column items-center text-weight-medium text-body1"
                >
                  <q-avatar icon="mdi-account" size="100px"></q-avatar>
                  {{ "Abdul Mueed Shahbaz" }}
                </q-card-section>
                <q-card-actions>
                  <q-btn outline :label="MAP.LOGIN"></q-btn>
                </q-card-actions>
              </q-card>
            </q-menu>
          </q-btn>
        </div> -->
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
import { APP_ROUTES } from "../common/constants/_routes";
import { COUPLED_APPS } from "../common/constants/app";
import { computed, getCurrentInstance, onMounted, ref } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { errorNotification } from "src/common/utils/notifications";

export default {
  components: {
    MainMenu,
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
    function getRequiredGlobals() {
      const appName = app.appContext.config.globalProperties.$appName;
      const loginAppUrl = app.appContext.config.globalProperties.$loginAppUrl;
      if (appName && loginAppUrl) {
        return { appName, loginAppUrl };
      }
    }
    function redirectToLogin() {
      const requiredGlobals = getRequiredGlobals();
      if (!requiredGlobals) {
        errorNotification("Service currently unavailable");
        return;
      }
      const queryStringObject = {
        app_name: requiredGlobals.appName,
        redirect_url: window.location.origin,
      };
      const queryString =
        "?" + new URLSearchParams(queryStringObject).toString();
      window.location.href = requiredGlobals.loginAppUrl + queryString;
    }
    function searchProducts(query) {
      $store.dispatch("products/search", { query }).then((res) => {
        if (res.length > 0) {
          $router.push(APP_ROUTES.SEARCH_RESULTS.NAME);
        }
      });
    }
    onMounted(() => {
      const currentDate = new Date();
      const currentTime = ~~(currentDate.getTime() / 1000);
      console.log(loginDetails.value.expiry - currentTime);
      if (loginDetails.value) {
        console.log(loginDetails.value.expiry, "expiry");
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
          $store.dispatch("login/getAuthDetails", queryObject);
          setTimeout(() => {
            window.location.href = window.location.origin;
          }, 1000);
          // window.location.href = window.location.origin;
          // TODO: Store auth token in store and set isAuthenticated to true and create persistent storage
          // window.location.href = window.location.origin;
        }
      }
    });

    return {
      redirectToLogin,
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
