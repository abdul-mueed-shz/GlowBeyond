<template>
  <div class="text-weight-medium text-secondary text-h4 text-center q-pt-xl">
    {{ MAP.HOMEPAGE.HOLIDAY_GIFT_GUIDE }}
  </div>
  <div
    class="row q-pt-lg q-gutter-y-md text-center text-grey-9"
    :class="$q.screen.gt.xs && 'q-px-lg'"
  >
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
