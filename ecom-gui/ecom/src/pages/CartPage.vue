<template>
  <q-page padding>
    <div id="title" class="text-h4 text-primary text-weight-medium">Cart</div>
    <q-separator class="q-mb-md"></q-separator>
    <div id="cartItems">
      <cart-items :rows="cartItems" :columns="columns" />
    </div>
    <div id="summary" class="q-mt-xl">
      <!--  -->
      <q-card class="full-width">
        <!--  -->
        <q-card-section>
          <div id="title" class="text-h4 text-primary text-weight-medium">
            Summary
          </div>
        </q-card-section>
        <q-separator inset class="q-mb-md bg-secondary"></q-separator>
        <q-card-section>
          <!--  -->
          <div class="column text-h6 text-weight-regular">
            <div class="row q-mb-lg">
              <div>{{ `Total Items: ${cartQuantity}` }}</div>
            </div>
            <div class="row">
              <div>{{ `Price: Rs ${getCartTotal}` }}</div>
            </div>
          </div>
        </q-card-section>
        <q-card-actions>
          <q-btn
            class="text-white bg-primary q-mb-md"
            label="Proceed to checkout"
          ></q-btn>
        </q-card-actions>
      </q-card>
    </div>
  </q-page>
</template>

<script>
import { computed } from "vue";
import { useStore } from "vuex";
import CartItems from "src/components/CartItems.vue";
export default {
  name: "CartPage",
  components: {
    "cart-items": CartItems,
    //
  },
  setup() {
    //
    const $store = useStore();
    const cartItems = computed(() => {
      return $store.getters["cart/getCartItems"];
    });
    const cartQuantity = computed(() => {
      return $store.getters["cart/getCartQuantity"];
    });
    const getCartTotal = computed(() => {
      return $store.getters["cart/getCartTotal"];
    });
    const columns = [
      {
        name: "id",
        align: "left",
        label: "Id",
        field: "id",
        sortable: true,
      },
      {
        name: "name",
        align: "left",
        label: "Name",
        field: "name",
        sortable: true,
      },
      {
        name: "price",
        label: "Price",
        field: (row) => +row.price,
        sortable: true,
        align: "left",
      },
      {
        name: "quantity",
        label: "Quantity",
        field: "quantity",
        sortable: true,
        align: "left",
      },
      {
        name: "totalPrice",
        label: "Total Price",
        field: (row) => row.price * row.quantity,
        sortable: true,
        align: "left",
      },
      {
        name: "remove",
        label: "Remove",
        field: () => {},
        sortable: true,
        align: "left",
      },
    ];
    //

    return {
      //
      cartItems,
      columns,
      cartQuantity,
      getCartTotal,
    };
  },
};
</script>
