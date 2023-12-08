<template>
  <div class="row">
    <div
      class="col-xs-12 col-sm-5 col-md-3 col-lg-2"
      id="products"
      v-for="product in products"
      :key="product.id"
    >
      <div class="q-px-sm">
        <q-card
          class="product-card full-width cursor-pointer full-height text-center"
          style="max-width: 300px"
          @click="toProductcategoryDetails(product)"
        >
          <q-card-section>
            <q-img
              style="max-width: 300px; height: 150px"
              :src="product.get_thumbnail"
            ></q-img>
          </q-card-section>
          <q-card-section class="product-details">
            <div class="q-mb-sm text-weight-medium">
              {{ product.name }}
            </div>
            <div class="q-mb-xs overflow-ellipsis cat-description">
              {{ product.description }}
            </div>
            <div class="q-pt-sm text-weight-bolder">
              {{ "Price: " + +product.price + " Rs" }}
            </div>
          </q-card-section>
        </q-card>
      </div>
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
