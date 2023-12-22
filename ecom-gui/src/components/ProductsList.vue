<template>
  <div class="row">
    <q-card
      flat
      class="col-xs-12 col-sm-5 col-md-3"
      id="products"
      v-for="product in products"
      :key="product.id"
    >
      <q-card-section>
        <q-img
          class="border-radius-top__6px height__400px cursor-pointer"
          :src="product.get_thumbnail"
          @click="() => toProductcategoryDetails(product)"
        ></q-img>
      </q-card-section>
      <q-card-section class="column items-center">
        <div>
          {{ product.name }}
        </div>
        <div class="q-py-sm">
          {{ +product.price + " Dhs" }}
        </div>
        <div
          class="text-grey-7 height__40px text-overflow__hidden-ellipsis max-width__420px text-center"
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
  </div>
</template>

<script>
import { toProductDetails, addToCart } from "src/common/utils/functions";
import { computed } from "vue";
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
    const store = useStore();
    const MAP = computed(() => {
      return store.getters["app/getMAP"];
    });

    const categories = store.getters["products/getCategories"];
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
      MAP,
      addToCart,
      toProductDetails,
    };
  },
};
</script>
