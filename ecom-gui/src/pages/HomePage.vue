<template>
  <q-page class="q-pb-md">
    <banner-item />
    <latest-products
      :latest-products="latestProducts"
      :latest-in-categories="latestInCategories"
    />
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
    const store = useStore();

    const latestInCategories = computed(() => {
      return store.getters["products/getCategories"];
    });

    const latestProducts = computed(() => {
      return store.getters["products/getLatestProducts"];
    });

    return {
      latestProducts,
      latestInCategories,
    };
  },
};
</script>
