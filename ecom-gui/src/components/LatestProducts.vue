<template>
  <div class="q-py-xl">
    <div v-for="category in props.latestInCategories" :key="category.id">
      <div class="text-secondary text-h4 text-center">
        Latest in {{ category.name }}
      </div>
      <div
        class="row justify-center q-pt-md"
        :class="$q.screen.gt.xs && 'q-px-lg'"
      >
        <product-item
          class="text-center text-grey-9"
          v-for="product in category.products"
          :key="product.name"
          :product="product"
        />
      </div>
    </div>
    <div class="text-secondary text-h4 text-center">
      {{ MAP.HOMEPAGE.LATESTPRODUCTS }}
    </div>
    <div
      class="row text-center text-grey-9 q-pt-md"
      :class="$q.screen.gt.xs && 'q-px-lg'"
    >
      <product-item
        v-for="product in props.latestProducts"
        :key="product.name"
        :product="product"
      />
    </div>
  </div>
</template>

<script setup>
import ProductItem from "./ProductItem.vue";
import { computed } from "vue";
import { useStore } from "vuex";
const $store = useStore();

const props = defineProps({
  latestInCategories: {
    type: Array,
    required: true,
  },
  latestProducts: {
    type: Array,
    required: true,
  },
});
const MAP = computed(() => {
  return $store.getters["app/getMAP"];
});
</script>
