import { api } from "src/boot/axios";
import { useGlobalRouter } from "src/boot/globals";

const $router = useGlobalRouter();

export async function fetchLatestProducts({ state, commit }) {
  try {
    const url = "products/";
    const products = await api.get(url);
    commit("setLatestProducts", products.data);
    return Promise.resolve();
  } catch (err) {
    console.log(err);
  }
}
export async function getProductDetails({ state, commit }, queryParams) {
  if (queryParams.category_slug && queryParams.product_slug) {
    try {
      const url = "products/product_details/";
      const res = await api.get(url, {
        params: queryParams,
      });
      commit("setSelectedProduct", res.data);
      return res.data;
    } catch (err) {
      throw new Error(err);
    }
  }
  return "INVALID PARAMS";
}

export async function fetchCategories({ state, commit }) {
  try {
    const url = "categories/";
    const categories = await api.get(url);
    commit("setCategories", categories.data);
    return categories.data;
  } catch (err) {
    throw new Error(err);
  }
}
export async function getCategoryDetails({ state, commit }, queryParams) {
  if (queryParams.category_slug) {
    try {
      const url = "categories/category_details/";
      const category_details = await api.get(url, { params: queryParams });
      return category_details.data;
    } catch (err) {
      console.log(err);
    }
    return;
  }
  return "INVALID PARAMS";
}
export async function search({ state, commit }, queryParams) {
  try {
    const url = "search/";
    const search_results = await api.post(url, queryParams);
    commit("setSearchedProduct", search_results.data);
    return search_results.data;
  } catch (err) {
    console.log(err);
  }
}
export async function consumedProducts({ commit }, payload) {
  try {
    const url = "consumed-products";
    const config = {
      params: payload.queryParams,
      headers: { AUTHTOKEN: payload.auth_token },
    };
    const result = await api.get(url, config);
    return result.data;
  } catch (err) {
    console.log(err);
  }
}
