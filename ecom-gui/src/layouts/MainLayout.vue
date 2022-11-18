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
            <q-icon name="mdi-magnify"></q-icon>
          </template>
        </q-input>

        <!-- <div id="logDetails">
          <q-btn outline icon="mdi-account" color="" :label="MAP.LOGIN">
            <q-menu fit>
              <q-card
                style="min-width: 280px"
                flat
                class="column text-primary flex-center q-mb-md"
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
import { computed, ref } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

export default {
  components: {
    MainMenu,
  },
  setup() {
    // CONSTANTS
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
