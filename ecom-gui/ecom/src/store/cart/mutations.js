/*
export function someMutation (state) {
}
*/
export function initializeCart(state) {
  if (localStorage.getItem("cartItems")) {
    state.items = JSON.parse(localStorage.getItem("cartItems"));
    return Promise.resolve();
  }
  localStorage.setItem("cartItems", JSON.stringify(state.items));
  return Promise.resolve();
}
export function setCartQuantity(state, quantity) {
  state.cartQuantity = quantity;
}
export function addToCart(state, payload) {
  try {
    const product = state.items.find(
      (item) => item.product.id === payload.product.id
    );
    if (product !== undefined) {
      product.quantity =
        parseInt(product.quantity) + parseInt(payload.quantity);
    } else {
      state.items.push(payload);
    }
    localStorage.setItem("cartItems", JSON.stringify(state.items));
    return Promise.resolve();
  } catch (err) {
    return Promise.reject(err);
  }
}
