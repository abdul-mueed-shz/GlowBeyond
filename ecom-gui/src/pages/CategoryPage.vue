<template>
  <q-page padding>
    <div id="title" class="text-h4 text-primary text-weight-medium q-px-md">
      {{ capitalizeFirstLetter(selectedCategory?.label) }}
    </div>
    <q-separator class="q-mb-md"></q-separator>
    <products-list :products="categoryDetails?.products ?? []" />
  </q-page>
</template>

<script>
import ProductsList from "src/components/ProductsList.vue";
import {
  capitalizeFirstLetter,
  getCategoryDetails,
} from "src/common/utils/functions";
import { computed, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
export default {
  components: {
    ProductsList,
  },
  setup() {
    const store = useStore();
    const route = useRoute();
    const categorySlug = route.params?.slug;

    const categoryDetails = ref({
      products: [],
    });
    const selectedCategory = computed(() => {
      const menu = store.getters["menu/getMenuList"];
      const selectedItem = menu.find(
        (item) => item?.link?.PARAMS?.slug === categorySlug
      );
      return selectedItem;
    });
    onMounted(() => {
      if (categorySlug) {
        getCategoryDetails(categorySlug).then((result) => {
          categoryDetails.value = result;
        });
      }
    });
    return {
      capitalizeFirstLetter,
      categoryDetails,
      selectedCategory,
    };
  },
  name: "SummerCollection",
};
</script>
