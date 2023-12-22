<template>
  <q-item
    dense
    clickable
    @click="() => navigate()"
    :active="$route.fullPath === currentRoute"
  >
    <q-item-section class="q-ml-sm text-weight-medium">
      {{ item.label }}
      {{ item.name === APP_ROUTES.CART.NAME ? `(${cartQuantity})` : "" }}
    </q-item-section>
  </q-item>
</template>

<script setup>
import { APP_ROUTES } from "src/common/constants/_routes";
import { computed } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
// Variables
const props = defineProps({
  item: {
    type: Object,
    required: true,
  },
});

const router = useRouter();
const store = useStore();

// Computed Properties
const currentRoute = computed(() => {
  const itemLink = props.item?.link;
  const route = itemLink?.NAME;
  let fullPath = "/" + route;
  for (const key in itemLink?.PARAMS) {
    fullPath += "/" + itemLink?.PARAMS[key];
  }
  return fullPath;
});
const item = computed(() => {
  return props.item;
});
const selectedMenuItem = computed(() => {
  return store.getters["menu/getSelectedMenuItem"];
});
const cartQuantity = computed(() => {
  return store.getters["cart/getCartQuantity"];
});
// Functions
function navigate() {
  router
    .push({
      name: item.value?.link?.NAME,
      params: item.value?.link?.PARAMS,
    })
    .then(() => {
      store.commit("menu/setSelectedMenuItem", item.value?.link?.NAME);
    });
}
</script>
