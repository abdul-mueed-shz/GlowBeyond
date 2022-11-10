/*
export function someAction (context) {
}
*/
export async function initializeCart({ state, commit }) {
  await commit("initializeCart");
  const cartQuantity = state.items.length;
  commit("setCartQuantity", cartQuantity);
  return Promise.resolve();
}

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
