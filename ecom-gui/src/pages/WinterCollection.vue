<template>
  <q-page padding>
    <div id="title" class="text-h4 text-primary text-weight-medium">
      {{ capitalizeFirstLetter($route.name) }}
    </div>
    <q-separator class="q-mb-md"></q-separator>

    <product-items :products="categoryDetails.products" />
  </q-page>
</template>

<script>
import ProductsList from "src/components/ProductsList.vue";
import {
  capitalizeFirstLetter,
  getCategoryDetails,
} from "src/common/utils/functions";
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
export default {
  components: {
    "product-items": ProductsList,
  },
  setup() {
    const $route = useRoute();
    const categoryDetails = ref({
      products: [],
    });
    onMounted(() => {
      getCategoryDetails($route.name).then((result) => {
        categoryDetails.value = result;
      });
    });
    return {
      capitalizeFirstLetter,
      categoryDetails,
    };
  },
  name: "SummerCollection",
};
</script>
