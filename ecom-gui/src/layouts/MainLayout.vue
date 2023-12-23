<!-- TODO: MAKE STORES PERSISTENT -->
<!-- TODO: IMPROVE UI -->
<!-- TODO: REPLACE CONSOLE LOGS WITH SHOWERROR OR SHOWSUCCESS UTIL FUNCTION CALLS -->
<!-- TODO: MAKE UTIL FUNCTIONS FOR CART ITEM DECREMENT INCREMENT AND REMOVAL IN CART ITEMS COMPONENT -->

<template>
  <q-layout view="lHh LpR lff">
    <q-header>
      <div class="bg-notif-message q-py-sm flex flex-center text-weight-medium">
        <span>{{
          bannerNotification.statement ?? "Free shipping above order 300 Dhs"
        }}</span>
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
            :src="getAppInfo.logo ?? '../assets/LOGO.png'"
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
        <AuthMenu v-if="false" />
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
      <q-ajax-bar ref="bar" position="bottom" color="primary" size="10px" />
      <router-view :key="$route.fullPath" />
      <q-page-sticky
        v-if="$route.name !== APP_ROUTES.CART.NAME"
        position="bottom-right"
        :offset="[18, 10]"
      >
        <div class="q-px-md q-pb-sm">
          <div class="relative-position">
            <div class="q-pb-sm">
              <q-avatar
                v-if="+cartQuantity > 0"
                color="negative"
                text-color="white"
                size="sm"
                class="absolute-top z-max"
                >{{ cartQuantity }}</q-avatar
              >
            </div>
            <q-fab icon="mdi-cart-outline" direction="up" color="primary">
              <q-fab-action
                color="primary"
                class="q-px-md text-caption"
                @click="$router.push({ name: APP_ROUTES.CART.NAME })"
              >
                <q-icon
                  name="mdi-cart-outline"
                  class="q-pr-xs"
                  size="sm"
                ></q-icon>
                Go to Cart
              </q-fab-action>
              <!--  -->
              <q-fab-action
                :disable="cartQuantity <= 0"
                color="primary"
                class="q-px-md text-caption"
                @click="() => $store.dispatch('cart/clearCart')"
              >
                <q-icon
                  name="mdi-cart-remove"
                  class="q-pr-xs"
                  size="sm"
                ></q-icon>
                Clear Cart
              </q-fab-action>
            </q-fab>
          </div>
        </div>
      </q-page-sticky>
    </q-page-container>

    <q-footer class="q-pt-md">
      <div
        class="q-pt-md q-pb-lg row q-gutter-y-md justify-center"
        style="padding-left: 10%; padding-right: 10%"
      >
        <div class="col-12 col-sm-3">
          <div class="text-h6 q-pb-md">Contact Us</div>
          <div class="column text-body1 q-gutter-y-sm">
            <div
              v-for="contact in getContactInfo"
              :key="contact.id"
              class="cursor-pointer underline"
            >
              {{ contact.info }}
            </div>
          </div>
        </div>
        <!-- <div class="col-12 col-sm-3">
          <div class="text-h6 q-pb-md">Help</div>
          <div class="column text-body1 q-gutter-y-sm">
            <div class="cursor-pointer">How to order</div>
            <div class="cursor-pointer">How to use gift card</div>
            <div class="cursor-pointer">Returns & Exchanges</div>
            <div class="cursor-pointer">Shipping Details</div>
            <div class="cursor-pointer">Privacy Policy</div>
            <div class="cursor-pointer">FAQs</div>
          </div>
        </div>
        <div class="col-12 col-sm-3">
          <div class="text-h6 q-pb-md">What's New</div>
          <div class="column text-body1 q-gutter-y-sm">
            <div class="cursor-pointer">Become a Brand Ambassador</div>
            <div class="cursor-pointer">Who made your chlothes</div>
            <div class="cursor-pointer">Shop Instagram</div>
          </div>
        </div> -->
        <div class="col-12 col-sm-3">
          <div class="text-h6 q-pb-md">Mailing Address</div>
          <div class="column text-body1 q-gutter-y-sm">
            <div
              v-for="mailing in getMailingInfo"
              :key="mailing.id"
              class="cursor-pointer underline"
            >
              {{ mailing.info }}
            </div>
          </div>
        </div>
      </div>

      <div class="q-mt-md q-pb-md bg-secondary flex flex-center q-pa-sm">
        <q-icon
          v-for="icon in getSocials"
          :key="icon.mdi_icon"
          :name="icon.mdi_icon"
          class="cursor-pointer q-px-md"
          size="sm"
          @click="() => openSocial(icon)"
        ></q-icon>
      </div>
    </q-footer>
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
    const toggleSearch = ref(false);
    const app = getCurrentInstance();

    const search = ref("");

    const store = useStore();

    const router = useRouter();

    const leftDrawerOpen = ref(false);

    // COMPUTED PROPERTIES
    const cartItems = computed(() => {
      return store.getters["cart/getCartItems"];
    });

    const cartQuantity = computed(() => {
      return store.getters["cart/getCartQuantity"];
    });

    const getSocials = computed(() => {
      return store.getters["appinfo/getSocials"];
    });

    const getAppInfo = computed(() => {
      return store.getters["appinfo/getAppInfo"];
    });

    const getMailingInfo = computed(() => {
      return store.getters["appinfo/getMailingInfo"];
    });

    const getContactInfo = computed(() => {
      return store.getters["appinfo/getContactInfo"];
    });

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

    const bannerNotification = computed(() => {
      return store.getters["appinfo/getBannerNotification"];
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

    async function setSocials() {
      store.dispatch("appinfo/setSocials");
    }

    async function setAppInfo() {
      store.dispatch("appinfo/setAppInfo");
    }

    async function setMailingInfo() {
      store.dispatch("appinfo/setMailingInfo");
    }

    async function setContactInfo() {
      store.dispatch("appinfo/setContactInfo");
    }

    async function setBannerNotification() {
      store.dispatch("appinfo/setBannerNotification");
    }

    function openSocial(icon) {
      window.open(icon.url);
    }

    onMounted(async () => {
      setSocials();
      setAppInfo();
      setMailingInfo();
      setContactInfo();
      setBannerNotification();
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
      search,
      getSocials,
      getAppInfo,
      getContactInfo,
      getMailingInfo,
      cartQuantity,
      cartItems,
      bannerNotification,
      toggleLeftDrawer,
      openSocial,
      searchProducts,
    };
  },
};
</script>
