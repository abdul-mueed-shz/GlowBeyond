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
