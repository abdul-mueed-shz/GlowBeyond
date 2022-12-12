<template>
  <q-page>
    <BannerItem />
    <LatestProducts :product-list="productList" />
  </q-page>
</template>

<script>
import { computed } from "vue";
import BannerItem from "../components/BannerItem.vue";
import LatestProducts from "../components/LatestProducts.vue";
import { useStore } from "vuex";

export default {
  components: {
    BannerItem,
    LatestProducts,
  },
  setup() {
    const $store = useStore();
    const productList = computed(() => {
      return $store.getters["products/getLatestProducts"];
    });

    return {
      productList,
    };
  },
};
</script>
