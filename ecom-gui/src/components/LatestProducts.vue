<template>
  <div class="text-weight-bold text-grey-9 text-h4 text-center q-ma-xl">
    {{ MAP.HOMEPAGE.LATESTPRODUCTS }}
  </div>
  <div class="row q-pa-lg q-gutter-y-md text-center text-grey-9">
    <product-item
      v-for="product in props.productList"
      :key="product.name"
      :product="product"
    />
  </div>
</template>

<script setup>
import ProductItem from "./ProductItem.vue";
import { computed } from "vue";
import { useStore } from "vuex";
const $store = useStore();

const props = defineProps({
  productList: {
    type: Array,
    required: true,
  },
});

const MAP = computed(() => {
  return $store.getters["app/getMAP"];
});
</script>
