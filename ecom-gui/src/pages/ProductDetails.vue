<template>
  <q-page padding class="q-px-xl text-grey-9">
    <q-card flat class="row q-pa-md border-radius__8px">
      <div class="col-12 col-sm-6">
        <q-carousel
          swipeable
          animated
          v-model="slide"
          thumbnails
          infinite
          style="height: 660px"
          autoplay
        >
          <q-carousel-slide
            v-for="(image, index) in product.get_images"
            :key="index"
            :name="index"
            :img-src="image"
          />
        </q-carousel>
      </div>
      <div class="col-12 col-sm-6 q-pa-md">
        <div class="text-h4">
          {{ product.name }}
        </div>
        <div class="q-mt-lg text-h5 q-mb-lg">
          {{ `Dhs ${+product.price}` }}
        </div>
        <q-form
          @submit.prevent="() => addToCart(product, quantity)"
          class="column q-gutter-y-md"
        >
          <div>
            <label for="quantity"> Quantity </label>
            <q-input
              id="quantity"
              dense
              label-color="primary"
              v-model="quantity"
              :rules="[(val) => !!val || 'Quantity is required']"
              outlined
              type="number"
            ></q-input>
          </div>
          <q-btn type="submit" label="Add to cart" color="primary"></q-btn>
          <div class="text-body1 text-grey-8">
            {{ product.description }}
          </div>
        </q-form>
      </div>
    </q-card>
  </q-page>
</template>

<script>
import { APP_CONSTANTS } from "src/common/constants/app";
import { addToCart } from "src/common/utils/functions";
import { computed, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
export default {
  setup() {
    // Variables
    const slide = ref(0);
    const quantity = ref(1);
    const store = useStore();
    const route = useRoute();
    // Computed Properties
    const product = computed(() => {
      return store.getters["products/getSelectedProduct"];
    });

    async function getDetails() {
      try {
        const { category: category_slug, product: product_slug } = route.query;
        const res = await store.dispatch("products/getProductDetails", {
          category_slug,
          product_slug,
        });
        return res;
      } catch (error) {
        console.log(error);
      }
    }

    onMounted(() => {
      getDetails();
    });

    // Functions/Variables/Properties exposed in the template
    return { slide, product, APP_CONSTANTS, quantity, addToCart };
  },
  name: "ProductDetails",
};
</script>
