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
        <div>
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
        </div>
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

<script setup>
import MainMenu from "src/components/MainMenu.vue";
import { APP_ROUTES } from "../common/constants/_routes";
import { computed, ref, watch } from "vue";
import { useStore } from "vuex";

// CONSTANTS
const $store = useStore();

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
</script>
