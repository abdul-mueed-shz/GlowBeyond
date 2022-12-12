<template>
  <q-page padding>
    <div class="row">
      <div class="col-6 text-h5 text-bold">Account details</div>
      <div class="col-6 text-h5 text-bold">
        <div class="q-ml-md">Coupons</div>
      </div>
    </div>
    <q-separator class="q-my-md" color="secondary"></q-separator>
    <div class="row">
      <div class="col-6 q-pr-sm">
        <q-card
          v-if="loginDetails"
          class="bg-primary text-white text-h6 full-width"
          style="height: 180px"
        >
          <q-card-section class="q-gutter-y-xs">
            <div class="row">
              <div class="col-10">
                <div class="q-pt-md">
                  <div>
                    Firstname:
                    <span class="text-weight-regular">{{
                      loginDetails.user_information.first_name
                    }}</span>
                  </div>
                  <div>
                    Lastname:
                    <span class="text-weight-regular">{{
                      loginDetails.user_information.last_name
                    }}</span>
                  </div>
                  <div>
                    Email:
                    <span class="text-weight-regular">{{
                      loginDetails.user_information.email
                    }}</span>
                  </div>
                </div>
              </div>
              <div class="col-2 text-white">
                <div class="flex justify-end">
                  <div>
                    <q-circular-progress
                      :value="100"
                      size="25px"
                      color="white"
                      center-color="green"
                      class="q-ma-md"
                    />
                  </div>
                  <div class="q-py-md">
                    <q-btn
                      color="secondary"
                      label="Logout"
                      @click="logout"
                    ></q-btn>
                  </div>
                </div>
              </div>
            </div>
          </q-card-section>
        </q-card>
      </div>
      <div class="col-6 q-pl-sm">
        <q-card
          v-if="loginDetails"
          class="bg-primary text-white text-h6 full-width"
          style="height: 180px"
        >
          <q-card-section v-if="coupons" class="q-gutter-y-xs row">
            <!--  -->
            <div class="col-4 q-pa-md">
              <div style="height: 110px" class="bg-white"></div>
            </div>
            <div class="col-4 q-pa-md">
              <div style="height: 110px" class="bg-white"></div>
            </div>
            <div class="col-4 q-pa-md">
              <div style="height: 110px" class="bg-white"></div>
            </div>
          </q-card-section>
          <q-card-section class="full-height flex flex-center" v-else>
            <div class="text-weight-regular">No coupons available!</div>
          </q-card-section>
        </q-card>
      </div>
    </div>
    <div class="q-mt-md text-h5 text-bold">Orders</div>
    <q-separator class="q-my-md" color="secondary"></q-separator>
    <div class="row" v-if="loginDetails">
      <div class="col-6" v-for="(order, index) in orders" :key="index">
        <div class="q-pr-md">
          <q-card class="bg-primary text-white">
            <q-card-section class="row text-h6">
              <div>
                <span> Order #: </span>
                <span class="text-weight-regular">
                  {{ index }}
                </span>
              </div>
              <q-space></q-space>
              <div class="q-mr-md">
                <span>Total Buyout:</span>
                <span class="q-ml-xs text-weight-regular">
                  {{ order.payed_amount }}Rs
                </span>
              </div>
            </q-card-section>
            <q-card-section class="row">
              <div
                class="col-6 q-pa-xs"
                v-for="product in order.products"
                :key="product.id"
              >
                <q-card>
                  <q-card-section>
                    <q-img
                      class="full-width"
                      style="max-width: 1000px; max-height: 250px"
                      :src="product.get_thumbnail"
                    ></q-img>
                  </q-card-section>
                  <q-card-section class="text-black">
                    <div class="row q-gutter-x-sm">
                      <div>
                        <span class="text-bold q-mr-xs">Name:</span
                        >{{ product.name }}
                      </div>
                      <div>
                        <span class="text-bold q-mr-xs">Price:</span
                        >{{ product.price }}
                      </div>
                      <div>
                        <span class="text-bold">Quantity Bought:</span
                        >{{ product.quantity }}
                      </div>
                    </div>
                  </q-card-section>
                </q-card>
              </div>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { computed, onMounted, ref, watch } from "vue";
import { useStore } from "vuex";
import { logout } from "src/common/utils/functions";
import { useRouter } from "vue-router";
import { APP_ROUTES } from "src/common/constants/_routes";

export default {
  name: "AccountDetails",
  setup() {
    const store = useStore();
    const router = useRouter();
    const coupons = ref(null);
    const orders = ref(null);

    const loginDetails = computed(() => {
      return store.getters["login/getLoginDetails"];
    });

    watch(loginDetails, (newValue, oldValue) => {
      if (!newValue) {
        router.push({ name: APP_ROUTES.HOME.NAME });
      }
    });

    onMounted(async () => {
      const payload = {
        auth_token: loginDetails.value.auth_token,
        queryParams: {
          id: loginDetails.value.user_information.id,
        },
      };
      const result = await store.dispatch("products/consumedProducts", payload);
      if (result) {
        orders.value = result;
      }
    });
    return {
      orders,
      loginDetails,
      logout,
      coupons,
    };
  },
};
</script>
