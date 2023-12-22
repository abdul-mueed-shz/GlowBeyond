<template>
  <q-card flat class="col-12 col-sm-6 col-md-3 full-height border-radius__12px">
    <q-card-section>
      <q-img
        @click="goToDetails"
        class="image-area border-radius-top__6px min-height__430px cursor-pointer"
        :src="product.get_thumbnail"
      ></q-img>
    </q-card-section>
    <q-card-section class="column q-py-none">
      <div>
        {{ product.name }}
      </div>
      <div class="q-py-md">
        {{ `${+product.price} Dhs` }}
      </div>
      <div
        class="text-grey-7 height__40px text-overflow__hidden-ellipsis max-width__420px"
      >
        {{ product.description }}
      </div>
    </q-card-section>
    <q-card-actions class="q-py-lg">
      <div class="full-width">
        <q-btn
          @click="addToCart(product, 1)"
          outline
          class="full-width"
          color="secondary"
          :label="MAP.HOMEPAGE.ADD_TO_BAG"
        ></q-btn>
      </div>
    </q-card-actions>
  </q-card>
</template>

<script setup>
import ProductItem from "./ProductItem.vue";
import { computed, ref } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { addToCart, toProductDetails } from "src/common/utils/functions";

const props = defineProps({
  product: {
    type: Object,
    required: true,
  },
});
const product = computed(() => {
  return props.product;
});
const categories = computed(() => {
  return $store.getters["products/getCategories"];
});

const $store = useStore();

const MAP = computed(() => {
  return $store.getters["app/getMAP"];
});

function goToDetails() {
  const category_slug = categories.value.find((category) => {
    return category.id === product.value.category;
  })["slug"];
  toProductDetails(product.value.slug, category_slug);
}
</script>

<style lang="scss">
.separator-width {
  max-width: 350px;
}
.image-area {
  max-width: 500px;
  max-height: 250px;
  height: 250px;
}
.prod-desc {
  max-height: 140px;
}
</style>
