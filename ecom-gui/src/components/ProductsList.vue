<template>
  <div class="row">
    <div
      class="col-xs-12 col-sm-5 col-md-3 col-lg-2 q-mr-md q-my-sm"
      id="products"
      v-for="product in products"
      :key="product.id"
    >
      <q-card
        class="product-card full-width cursor-pointer full-height text-center"
        style="max-width: 300px"
        @click="toProductcategoryDetails(product)"
      >
        <q-card-section>
          <q-img
            style="max-width: 300px; max-height: 190px"
            :src="product.get_thumbnail"
          ></q-img>
        </q-card-section>
        <q-card-section>
          <div class="q-mb-sm text-weight-medium">
            {{ product.name }}
          </div>
          <q-separator class="q-mb-xs"></q-separator>
          <div class="q-mb-xs">
            {{ product.description }}
          </div>
          <div>
            {{ "Price: " + +product.price + " Rs" }}
          </div>
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>

<script>
import { toProductDetails } from "src/common/utils/functions";
import { useStore } from "vuex";
export default {
  name: "CategoryItems",
  props: {
    products: {
      type: Object,
      required: true,
    },
  },
  setup() {
    const $store = useStore();
    const categories = $store.getters["products/getCategories"];
    function toProductcategoryDetails(product) {
      try {
        const category_slug = categories.find(
          (category) => category.id === product.category
        )["slug"];
        toProductDetails(product.slug, category_slug);
      } catch (err) {
        console.log(err);
      }
    }
    return {
      toProductcategoryDetails,
    };
  },
};
</script>

<style scoped lang="scss">
.product-card:hover {
  background: rgb(216, 216, 216);
}
</style>
