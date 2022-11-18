<template>
  <q-page padding>
    <q-card class="row q-pa-md">
      <div class="col-7">
        <q-img
          class="full-width"
          style="max-width: 1000px; max-height: 700px"
          :src="product.get_thumbnail"
        ></q-img>
      </div>
      <div class="col-5 q-pa-md">
        <div class="text-h4 text-weight-bold text-grey-9">
          {{ APP_CONSTANTS.INFORMATION }}
        </div>
        <div class="q-mt-lg text-h5 text-grey-9 q-mb-lg">
          {{ `${APP_CONSTANTS.PRICE}: ${+product.price} Rs ` }}
        </div>
        <div class="row q-gutter-x-md">
          <q-input
            class="col bg-grey-4"
            label="Quantity"
            label-color="primary"
            v-model="quantity"
            filled
            type="number"
          ></q-input>
          <q-btn
            @click="addToCart(product, quantity)"
            class="col"
            label="Add to cart"
            color="primary"
          ></q-btn>
        </div>
      </div>
    </q-card>
    <div class="Column q-my-md q-gutter-y-sm">
      <div class="text-h4 text-weight-bold text-grey-9">
        {{ product.name }}
      </div>
      <div class="text-h5 text-grey-9">
        {{ product.description }}
      </div>
    </div>
  </q-page>
</template>

<script>
import { APP_CONSTANTS } from "src/common/constants/app";
import { addToCart } from "src/common/utils/functions";
import { computed, ref } from "vue";
import { useStore } from "vuex";
export default {
  setup() {
    // Variables
    const quantity = ref(1);
    const $store = useStore();

    // Computed Properties
    const product = computed(() => {
      return $store.getters["products/getSelectedProduct"];
    });

    // Functions/Variables/Properties exposed in the template
    return { product, APP_CONSTANTS, quantity, addToCart };
  },
  name: "ProductDetails",
};
</script>
