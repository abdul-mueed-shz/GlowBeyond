<template>
  <q-icon id="loginDetails" class="q-ml-md" size="sm" name="mdi-account">
    <q-menu class="bg-primary" style="width: 300px" fit>
      <q-card class="flex flex-center bg-primary text-white">
        <!--  -->
        <q-card-section v-if="loginDetails" class="column">
          <!--  -->
          <q-btn no-caps @click="toAccountDetails" flat>
            <div class="q-my-md">
              <div>
                <span class="text-weight-bold">Email: </span>
                <span>
                  {{ loginDetails.user_information.email }}
                </span>
              </div>
            </div>
            <div class="q-mb-md">
              <div>
                <span class="text-weight-bold">Fullname: </span>
                <span>
                  {{ getFullName() }}
                </span>
              </div>
            </div>
          </q-btn>
          <q-separator color="white"></q-separator>
          <div class="q-mt-md q-mb-sm">
            <div @click="logout" class="row flex flex-center cursor-pointer">
              <q-icon name="mdi-logout" size="25px"></q-icon>
              <div style="font-size: medium" class="q-ml-sm text-weight-medium">
                Logout
              </div>
            </div>
          </div>
        </q-card-section>
        <q-card-section v-else>
          <div
            @click="redirectToLogin"
            class="row flex flex-center cursor-pointer"
          >
            <q-icon name="mdi-login" class="q-my-md" size="25px"></q-icon>
            <div style="font-size: large" class="q-ml-sm text-weight-medium">
              Login
            </div>
          </div>
        </q-card-section>
      </q-card>
    </q-menu>
  </q-icon>
</template>

<script>
import { computed, getCurrentInstance } from "vue";
import { useStore } from "vuex";
import { errorNotification } from "src/common/utils/notifications";
import { useRouter } from "vue-router";
import { APP_ROUTES } from "src/common/constants/_routes";

export default {
  name: "AuthenticationDetails",
  setup() {
    // Variables
    const $store = useStore();
    const $router = useRouter();
    const app = getCurrentInstance();

    // Computed Properties
    const loginDetails = computed(() => {
      return $store.getters["login/getLoginDetails"];
    });

    // Functions
    function getRequiredGlobals() {
      const appName = app.appContext.config.globalProperties.$appName;
      const loginAppUrl = app.appContext.config.globalProperties.$loginAppUrl;
      if (appName && loginAppUrl) {
        return { appName, loginAppUrl };
      }
    }
    function redirectToLogin() {
      const requiredGlobals = getRequiredGlobals();
      if (!requiredGlobals) {
        errorNotification("Service currently unavailable");
        return;
      }
      const queryStringObject = {
        app_name: requiredGlobals.appName,
        redirect_url: window.location.origin,
      };
      const queryString =
        "?" + new URLSearchParams(queryStringObject).toString();
      window.location.href = requiredGlobals.loginAppUrl + queryString;
    }
    async function logout() {
      $store.dispatch("login/callLogout");
      $store.dispatch("login/setLoginDetails", null);
      const intervalId = $store.getters["login/getIntervalId"];
      clearInterval(intervalId);
      $store.dispatch("login/setIntervalId", null);
    }
    function getFullName() {
      return (
        loginDetails.value.user_information.first_name +
        " " +
        loginDetails.value.user_information.last_name
      );
    }
    function toAccountDetails() {
      $router.push({ name: APP_ROUTES.ACCOUNT_DETAILS.NAME });
    }

    // Exposed properties
    return {
      redirectToLogin,
      logout,
      getFullName,
      loginDetails,
      toAccountDetails,
    };
  },
};
</script>
