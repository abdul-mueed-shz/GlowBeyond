<template>
  <q-item
    clickable
    active-class="bg-white text-primary"
    @click="navigate"
    :active="selectedMenuItem === item.name"
  >
    <q-item-section avatar>
      <q-avatar :size="item.icon.size" :icon="item.icon.name"></q-avatar>
    </q-item-section>
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

const $router = useRouter();
const $store = useStore();

// Computed Properties
const item = computed(() => {
  return props.item;
});
const selectedMenuItem = computed(() => {
  return $store.getters["menu/getSelectedMenuItem"];
});
const cartQuantity = computed(() => {
  return $store.getters["cart/getCartQuantity"];
});

// Functions
function navigate() {
  $store.commit("menu/setSelectedMenuItem", item.value.name);
  $router.push(item.value.link);
}
</script>
