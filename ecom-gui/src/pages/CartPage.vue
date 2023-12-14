<template>
  <q-page padding>
    <div id="title" class="text-h4 text-primary text-weight-medium q-px-md">
      {{ MAP.CART_PAGE["TITLE"] }}
    </div>
    <q-separator class="q-mb-md"></q-separator>
    <div id="cartItems">
      <cart-items
        :is-checking-out="onCheckout"
        :rows="cartItems"
        :columns="columns"
      />
    </div>
    <div id="cart-state" class="q-mt-xl">
      <q-card flat bordered id="summary" class="full-width border-radius__12px">
        <q-card-section class="text-h4 text-primary text-weight-medium">
          <div v-if="!onCheckout" id="summary-title">
            {{ MAP.CART_PAGE.CARD_TITLES["SUMMARY"] }}
          </div>
          <div v-else id="checkout-title">
            {{ MAP.CART_PAGE.CARD_TITLES["CHECKOUT"] }}
          </div>
        </q-card-section>
        <q-separator inset class="q-mb-md bg-secondary"></q-separator>
        <q-card-section id="quantity-container">
          <div class="column text-h6 text-weight-regular">
            <div class="row q-mb-lg">
              <div>{{ `Total Items: ${cartQuantity}` }}</div>
            </div>
            <div class="row">
              <div>{{ `Price: Rs ${getCartTotal}` }}</div>
            </div>
          </div>
        </q-card-section>
        <q-form @submit="checkOut">
          <q-card-section v-if="onCheckout" id="checkout-inputs">
            <div class="q-mb-md text-h6 text-weight-regular text-primary">
              * All fields are mandatory
            </div>
            <div class="row q-gutter-y-xs">
              <div class="col-12 col-sm-4 q-px-sm">
                <q-input
                  class="border-radius__8px"
                  dense
                  clearable
                  v-model="formData.first_name"
                  outlined
                  :label="MAP.INPUTS_LABELS['FIRST_NAME']"
                  :rules="[
                    (val) =>
                      !!val || `${MAP.INPUTS_LABELS['FIRST_NAME']} is required`,
                  ]"
                />
              </div>
              <div class="col-12 col-sm-4 q-px-sm">
                <q-input
                  class="border-radius__8px"
                  dense
                  clearable
                  v-model="formData.last_name"
                  outlined
                  :label="MAP.INPUTS_LABELS['LAST_NAME']"
                  :rules="[
                    (val) =>
                      !!val || `${MAP.INPUTS_LABELS['LAST_NAME']} is required`,
                  ]"
                />
              </div>
              <div class="col-12 col-sm-4 q-px-sm">
                <q-input
                  class="border-radius__8px"
                  dense
                  clearable
                  v-model="formData.email"
                  outlined
                  :label="MAP.INPUTS_LABELS['EMAIL']"
                  :rules="[
                    (val) =>
                      !!val || `${MAP.INPUTS_LABELS['EMAIL']} is required`,
                  ]"
                />
              </div>
              <div class="col-12 col-sm-4 q-px-sm">
                <q-input
                  class="border-radius__8px"
                  dense
                  clearable
                  v-model="formData.phone"
                  type="number"
                  outlined
                  :label="MAP.INPUTS_LABELS['PHONE']"
                  :rules="[
                    (val) =>
                      !!val || `${MAP.INPUTS_LABELS['PHONE']} is required`,
                  ]"
                />
              </div>
              <div class="col-12 col-sm-4 q-px-sm">
                <q-input
                  class="border-radius__8px"
                  dense
                  clearable
                  v-model="formData.address"
                  outlined
                  :label="MAP.INPUTS_LABELS['ADDRESS']"
                  :rules="[
                    (val) =>
                      !!val || `${MAP.INPUTS_LABELS['ADDRESS']} is required`,
                  ]"
                />
              </div>
              <div class="col-12 col-sm-4 q-px-sm">
                <q-input
                  class="border-radius__8px"
                  dense
                  clearable
                  v-model="formData.city"
                  outlined
                  :label="MAP.INPUTS_LABELS['PLACE']"
                  :rules="[
                    (val) =>
                      !!val || `${MAP.INPUTS_LABELS['PLACE']} is required`,
                  ]"
                />
              </div>
              <div class="col-12 col-sm-4 q-px-sm">
                <q-input
                  class="border-radius__8px"
                  dense
                  clearable
                  v-model="formData.zip_code"
                  outlined
                  type="number"
                  :label="MAP.INPUTS_LABELS['ZIP']"
                  :rules="[
                    (val) => !!val || `${MAP.INPUTS_LABELS['ZIP']} is required`,
                  ]"
                />
              </div>
            </div>
          </q-card-section>
          <q-card-actions>
            <q-btn
              v-if="!onCheckout"
              @click="toggleCheckout(true)"
              class="text-white bg-primary q-mb-md"
              style="width: 180px"
              :label="MAP.BTN['CHECKOUT']"
            ></q-btn>
            <div v-else class="q-ml-md q-gutter-x-sm">
              <q-btn
                @click="toggleCheckout(false)"
                class="text-white bg-negative q-mb-md btn-measurements border-radius__8px"
                :label="MAP.BTN['CANCEL']"
              ></q-btn>
              <q-btn
                type="submit"
                class="text-white bg-primary q-mb-md btn-measurements border-radius__8px"
                :label="MAP.BTN['PAY']"
              ></q-btn>
            </div>
          </q-card-actions>
        </q-form>
      </q-card>
    </div>
  </q-page>
</template>

<script>
import { computed, reactive, ref } from "vue";
import { useQuasar } from "quasar";
import { useStore } from "vuex";
import CartItems from "src/components/CartItems.vue";
import SuccessDialog from "src/components/SuccessDialog.vue";
import { errorNotification } from "src/common/utils/notifications";
export default {
  name: "CartPage",
  components: {
    "cart-items": CartItems,
  },
  setup() {
    // Variables
    const $store = useStore();
    const onCheckout = ref(false);
    const $q = useQuasar();
    const formData = reactive({
      first_name: null,
      last_name: null,
      email: null,
      phone: null,
      address: null,
      zip_code: null,
      city: null,
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
    // Computed properties

    const MAP = computed(() => {
      return $store.getters["app/getMAP"];
    });
    const cartItems = computed(() => {
      return $store.getters["cart/getCartItems"];
    });
    const cartQuantity = computed(() => {
      return $store.getters["cart/getCartQuantity"];
    });
    const getCartTotal = computed(() => {
      return $store.getters["cart/getCartTotal"];
    });
    const loginDetails = computed(() => {
      return $store.getters["login/getLoginDetails"];
    });

    // Functions
    function toggleCheckout(val) {
      if (!val) {
        return;
      }
      if (!cartQuantity.value) {
        errorNotification("No items in cart");
        return;
      }
      // if (!loginDetails.value) {
      //   errorNotification("Unauthenticated! Please login");
      //   return;
      // }
      onCheckout.value = val;
    }

    async function checkOut() {
      if (!cartQuantity.value) {
        errorNotification("No items in cart");
        return;
      }
      const payload = {
        data: {
          customer: formData,
          products: cartItems.value,
          order: {
            paid_amount: getCartTotal.value,
          },
        },
      };
      await $store.dispatch("cart/checkout", payload);
      onCheckout.value = false;
      successfulBuyOutDialog();
    }
    function successfulBuyOutDialog() {
      $q.dialog({
        component: SuccessDialog,
        componentProps: {
          text: "Purchase successful !",
        },
      });
    }

    return {
      cartItems,
      columns,
      cartQuantity,
      getCartTotal,
      onCheckout,
      toggleCheckout,
      MAP,
      checkOut,
      formData,
    };
  },
};
</script>
