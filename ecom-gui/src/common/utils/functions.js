import { APP_ROUTES } from "../../common/constants/_routes";
import { useGlobalRouter, useGlobalStore } from "src/boot/globals";

const $store = useGlobalStore();
const $router = useGlobalRouter();

export function getCategoryDetails(category_slug) {
  const queryParams = { category_slug };
  return $store.dispatch("products/getCategoryDetails", queryParams);
}

export async function toProductDetails(product_slug, category_slug) {
  try {
    const queryParams = { category_slug, product_slug };
    await $store.dispatch("products/getProductDetails", queryParams);
    $router.push({ name: APP_ROUTES.PRODUCT_DETAILS.NAME });
  } catch (error) {
    console.log(error);
  }
}

export function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.substring(1);
}
