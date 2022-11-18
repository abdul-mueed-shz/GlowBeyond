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
            @click="addToCart"
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
import {
  successNotification,
  errorNotification,
} from "src/common/utils/notifications";
import { computed, onMounted, ref } from "vue";
import { useStore } from "vuex";
export default {
  setup() {
    // Variables
    const quantity = ref(1);
    const $store = useStore();

    // Computed Propert
    const product = computed(() => {
      return $store.getters["products/getSelectedProduct"];
    });

    // Functions
    async function addToCart() {
      // CREATE UTIL FUNCTION OF THIS. PASS argument quantity as quanity.value and product as product.value
      try {
        const payload = {
          ...product.value,
          quantity: quantity.value,
          // quantity: quantity.value,
        };
        await $store.dispatch("cart/addToCart", payload);
        successNotification("Product Added to cart");
      } catch (err) {
        errorNotification("Failed to add to cart");
        console.log(err);
      }
    }

    return { product, APP_CONSTANTS, quantity, addToCart };
  },
  // name: 'PageName',
};
</script>
