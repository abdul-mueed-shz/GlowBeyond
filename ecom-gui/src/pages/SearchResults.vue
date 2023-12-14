<template>
  <q-page padding>
    <div id="title" class="text-h4 text-primary text-weight-medium">
      {{ searchLength }}
    </div>
    <q-separator class="q-mb-md"></q-separator>
    <products-list :products="resultList" />
  </q-page>
</template>

<script>
import ProductsList from "src/components/ProductsList.vue";
import { computed } from "vue";
import { useStore } from "vuex";
import { APP_CONSTANTS } from "src/common/constants/app";
export default {
  components: {
    ProductsList,
  },
  name: "SearchResults",
  setup() {
    const $store = useStore();
    const resultList = computed(() => {
      return $store.getters["products/getSearchedProduct"];
    });
    const searchLength = computed(() => {
      return `${APP_CONSTANTS.SEARCH_RESULTS} : ${resultList.value.length}`;
    });
    return {
      resultList,
      searchLength,
    };
  },
};
</script>
