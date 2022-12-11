import { api } from "src/boot/axios";
import { errorNotification } from "src/common/utils/notifications";

export async function addToCart({ state, commit }, payload) {
  try {
    await commit("addToCart", payload);
    const cartQuantity = state.items.length;
    commit("setCartQuantity", cartQuantity);
    return Promise.resolve();
  } catch (err) {
    return Promise.reject(err);
  }
}
export async function removeFromCart({ state, commit }, payload) {
  try {
    await commit("removeFromCart", payload);
    const cartQuantity = state.items.length;
    commit("setCartQuantity", cartQuantity);
    return Promise.resolve();
  } catch (err) {
    return Promise.reject(err);
  }
}
export async function deleteFromCart({ state, commit }, payload) {
  try {
    await commit("deleteFromCart", payload);
    const cartQuantity = state.items.length;
    commit("setCartQuantity", cartQuantity);
    return Promise.resolve();
  } catch (err) {
    return Promise.reject(err);
  }
}
export async function checkout({ commit }, payload) {
  try {
    const url = "checkout";
    const response = await api.post(url, payload.data, {
      headers: { AUTHTOKEN: payload.auth_token },
    });
    commit("clearCart");
    return response.data;
  } catch (err) {
    console.log(err);
    errorNotification(err.response.data);
  }
}
export async function clearCart({ commit }) {
  commit("clearCart");
}
