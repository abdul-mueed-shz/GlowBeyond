<template>
  <q-table
    class="border-radius__12px q-pt-md text-grey-8"
    flat
    bordered
    :rows="rows"
    :columns="columns"
  >
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
      <q-tr :props="props" class="text-weight-medium">
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
            @click="addToCart(props.row, 1)"
          ></q-btn>
          <q-btn
            flat
            color="negative"
            round
            size="xs"
            icon="mdi-minus"
            @click="decrementFromCart(props.row, 1)"
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
            @click="deleteFromCart(props.row)"
          ></q-btn>
        </q-td>
      </q-tr>
    </template>
  </q-table>
</template>

<script>
import {
  addToCart,
  decrementFromCart,
  deleteFromCart,
} from "src/common/utils/functions";
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
    isCheckingOut: {
      type: Boolean,
      required: true,
    },
  },
  setup() {
    return {
      addToCart,
      decrementFromCart,
      deleteFromCart,
    };
  },
};
</script>
