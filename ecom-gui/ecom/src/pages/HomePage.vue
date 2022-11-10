<template>
  <q-page>
    <BannerItem />
    <LatestProducts :product-list="productList" />
  </q-page>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import BannerItem from "../components/BannerItem.vue";
import LatestProducts from "../components/LatestProducts.vue";
import { useStore } from "vuex";
import { useRoute } from "vue-router";
const $store = useStore();

const productList = computed(() => {
  return $store.getters["products/getLatestProducts"];
});

onMounted(async () => {
  await $store.dispatch("cart/initializeCart");
  await $store.dispatch("products/fetchLatestProducts");
  await $store.dispatch("products/fetchCategories");
});
</script>
