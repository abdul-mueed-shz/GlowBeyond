<template>
  <div class="col-12 col-sm-6 col-md-3 q-pa-md">
    <q-card flat class="full-height border-radius__12px cursor-pointer">
      <q-card-section>
        <q-img
          @click="goToDetails"
          class="image-area"
          :src="product.get_thumbnail"
          style="min-height: 430px"
        ></q-img>
      </q-card-section>
      <q-card-section class="column q-py-none">
        <div class="q-pb-lg">
          {{ product.name }}
        </div>
        <div>
          {{ `${+product.price}Dhs` }}
        </div>
        <div class="text-grey-7">
          <div class="overflow-ellipsis prod-desc">
            {{ product.description }}
          </div>
        </div>
      </q-card-section>
      <q-card-actions class="q-py-lg">
        <div class="full-width">
          <q-btn
            @click="addToCart(product, 1)"
            outline
            class="full-width"
            color="secondary"
            :label="MAP.HOMEPAGE.ADD_TO_BAD"
          ></q-btn>
        </div>
      </q-card-actions>
    </q-card>
  </div>
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
const $router = useRouter();

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
