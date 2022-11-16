<template>
  <q-table :rows="rows" :columns="columns">
    <!--  -->
    <template #header="props">
      <q-tr :props="props">
        <q-th
          v-for="col in props.cols"
          :key="col.name"
          :props="props"
          class="text-primary"
        >
          {{ col.label }}
        </q-th>
      </q-tr>
    </template>
    <template #body="props">
      <q-tr :props="props" class="text-secondary text-weight-medium">
        <q-td key="id" :props="props">
          {{ props.row.id }}
        </q-td>
        <q-td key="name" :props="props">
          {{ props.row.name }}
        </q-td>
        <q-td key="price" :props="props">
          {{ +props.row.price }}
        </q-td>
        <q-td key="quantity" :props="props">
          {{ props.row.quantity }}
          <q-btn
            flat
            color="positive"
            round
            size="xs"
            icon="mdi-plus"
            @click="incrementProductQuantity(props.row)"
          ></q-btn>
          <q-btn
            flat
            color="negative"
            round
            size="xs"
            icon="mdi-minus"
            @click="decrementProductQuantity(props.row)"
          ></q-btn>
        </q-td>
        <q-td key="quantity" :props="props">
          {{ props.row.quantity * props.row.price }}
        </q-td>
        <q-td key="id" :props="props">
          <q-btn
            flat
            color="negative"
            round
            size="sm"
            icon="mdi-delete"
            @click="removeFromCart(props.row)"
          ></q-btn>
        </q-td>
      </q-tr>
    </template>
  </q-table>
</template>

<script>
import { useStore } from "vuex";
import {
  successNotification,
  errorNotification,
} from "src/common/utils/notifications";
export default {
  name: "CartItems",
  props: {
    rows: {
      type: Object,
      required: true,
    },
    columns: {
      type: Object,
      required: true,
    },
  },
  setup() {
    const $store = useStore();
    function removeFromCart(product) {
      console.log(product);
    }
    async function incrementProductQuantity(product) {
      // CREATE UTIL FUNCTION OF THIS. PASS ARGUMENT quantiy 1 and product
      try {
        const payload = {
          ...product,
          quantity: 1,
        };
        await $store.dispatch("cart/addToCart", payload);
        successNotification("Product Added to cart");
      } catch (err) {
        errorNotification("Failed to add to cart");
        console.log(err);
      }
      console.log(product);
    }
    function decrementProductQuantity(product) {
      console.log(product);
    }
    return {
      removeFromCart,
      incrementProductQuantity,
      decrementProductQuantity,
    };
  },
};
</script>
