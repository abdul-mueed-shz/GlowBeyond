/*
export function someAction (context) {
}
*/
import { api } from "src/boot/axios";

export async function fetchLatestProducts({ state, commit }) {
  try {
    const products = await api.get("products/");
    commit("setLatestProducts", products.data);
    return Promise.resolve();
  } catch (error) {
    console.log(error);
  }
}
export async function fetchCategories({ state, commit }) {
  try {
    const categories = await api.get("categories/");
    commit("setCategories", categories.data);
    return Promise.resolve();
  } catch (error) {
    console.log(error);
  }
}

export async function getProductDetails({ state, commit }, queryParams) {
  // $store.dispatch("products/getProductDetails", {
  //   category_slug: "summer",
  //   product_slug: "t-shirt",
  // });
  // products/product_details/?category_slug=summer&&product_slug=t-shirt
  if (
    queryParams.category_slug === undefined ||
    queryParams.product_slug === undefined
  ) {
    return;
  }
  try {
    const product_detail = await api.get("products/product_details/", {
      params: queryParams,
    });
    console.log(product_detail.data);
    commit("setSelectedProduct", product_detail.data);
    return Promise.resolve();
  } catch (error) {
    console.log(error);
  }
}
