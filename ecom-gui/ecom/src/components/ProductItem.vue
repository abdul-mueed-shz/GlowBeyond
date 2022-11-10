<template>
  <div class="col-12 col-sm-6 col-md-4 q-pa-md">
    <q-card class="full-height">
      <q-card-section>
        <q-img class="image-area" :src="product.get_thumbnail"></q-img>
        <!-- <q-img src="../assets/demo.jpg"></q-img> -->
      </q-card-section>
      <q-card-section class="column">
        <div class="text-h4 text-weight-medium">
          {{ product.name }}
        </div>
        <q-separator class="bg-grey-5 q-ma-sm" inset></q-separator>
        <div class="text-body1 text-weight-medium">
          {{ product.description }}
          <div class="flex flex-center">
            <q-separator
              class="full-width bg-grey-5 q-ma-sm flex separator-width"
              inset
            ></q-separator>
          </div>
          {{ `${+product.price} Rs` }}
        </div>
      </q-card-section>
      <q-card-actions class="flex flex-center q-pb-lg">
        <q-btn
          @click="toProductDetails"
          color="primary"
          :label="MAP.HOMEPAGE.VIEWDETAILS"
        ></q-btn>
      </q-card-actions>
    </q-card>
  </div>
</template>

<script setup>
import ProductItem from "./ProductItem.vue";
import { computed, ref } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { APP_ROUTES } from "../common/constants/_routes";

const props = defineProps({
  product: {
    type: Object,
    required: true,
  },
});

const $store = useStore();
const $router = useRouter();
const categories = computed(() => {
  return $store.getters["products/getCategories"];
});

const product = computed(() => {
  return props.product;
});

const MAP = computed(() => {
  return $store.getters["app/getMAP"];
});

async function toProductDetails() {
  try {
    const category_slug = categories.value.find((category) => {
      return category.id === product.value.category;
    })["slug"];
    const product_slug = props.product.slug;
    const queryParams = { category_slug, product_slug };
    await $store.dispatch("products/getProductDetails", queryParams);
    $router.push({ name: APP_ROUTES.PRODUCT_DETAILS.NAME });
  } catch (error) {
    console.log(error);
  }
}
</script>

<style lang="scss">
.separator-width {
  max-width: 350px;
}
.image-area {
  max-width: 500px;
  max-height: 300px;
}
</style>
