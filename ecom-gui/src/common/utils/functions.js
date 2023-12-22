import { APP_ROUTES } from "../../common/constants/_routes";
import { useGlobalRouter, useGlobalStore } from "src/boot/globals";
import {
  successNotification,
  errorNotification,
} from "src/common/utils/notifications";

const $store = useGlobalStore();
const $router = useGlobalRouter();

export function getCategoryDetails(category_slug) {
  // Takes in the category slug to pass as a query parameter for the api call
  const queryParams = { category_slug };
  return $store.dispatch("products/getCategoryDetails", queryParams);
}

export async function toProductDetails(product_slug, category_slug) {
  // Takes in the product and category slug to pass as a query parameter for the api call
  // On success routes to the productDetails page
  $router.push({
    name: APP_ROUTES.PRODUCT_DETAILS.NAME,
    query: { category: category_slug, product: product_slug },
  });
  try {
    // const queryParams = { category_slug, product_slug };
    // await $store.dispatch("products/getProductDetails", queryParams);
  } catch (error) {
    console.log(error);
  }
}

export function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.substring(1);
}

export async function addToCart(product, quantity = 1) {
  // CREATE UTIL FUNCTION OF THIS. PASS argument quantity as quanity.value and product as product.value
  try {
    const payload = {
      ...product,
      quantity,
    };
    await $store.dispatch("cart/addToCart", payload);
    successNotification("Product Added to cart");
  } catch (err) {
    errorNotification("Failed to add to cart");
  }
}

export async function decrementFromCart(product, quantity = 1) {
  try {
    const payload = {
      ...product,
      quantity,
    };
    await $store.dispatch("cart/removeFromCart", payload);
    successNotification("Product removed from cart");
  } catch (err) {
    errorNotification("Failed to remove from cart");
  }
}

export async function deleteFromCart(product) {
  try {
    await $store.dispatch("cart/deleteFromCart", product);
    successNotification("Product removed from cart");
  } catch (err) {
    errorNotification("Failed to remove from cart");
  }
}
export async function logout() {
  $store.dispatch("login/callLogout");
  $store.dispatch("login/setLoginDetails", null);
  const intervalId = $store.getters["login/getIntervalId"];
  clearInterval(intervalId);
  $store.dispatch("login/setIntervalId", null);
}

function getRequiredGlobals(app) {
  const appName = app.appContext.config.globalProperties.$appName;
  const loginAppUrl = app.appContext.config.globalProperties.$loginAppUrl;
  if (appName && loginAppUrl) {
    return { appName, loginAppUrl };
  }
}
export function redirectToLogin(app) {
  const requiredGlobals = getRequiredGlobals(app);
  if (!requiredGlobals) {
    errorNotification("Service currently unavailable");
    return;
  }
  const queryStringObject = {
    app_name: requiredGlobals.appName,
    redirect_url: window.location.origin,
  };
  const queryString = "?" + new URLSearchParams(queryStringObject).toString();
  window.location.href = requiredGlobals.loginAppUrl + queryString;
}
