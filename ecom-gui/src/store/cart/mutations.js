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
    const product = state.items.find((item) => item.id === payload.id);
    if (product) {
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
export function removeFromCart(state, payload) {
  try {
    const productIndex = state.items.map((item) => item.id).indexOf(payload.id);
    const productQuantity = +state.items[productIndex].quantity;
    const payLoadQuantity = +payload.quantity;
    if (productQuantity <= 1) {
      state.items.splice(productIndex, 1);
      localStorage.setItem("cartItems", JSON.stringify(state.items));
      return Promise.resolve();
    }
    if (payLoadQuantity < 0 || payLoadQuantity > productQuantity) {
      console.log("Bad Request");
      return Promise.reject("Bad Request");
    }
    state.items[productIndex].quantity = productQuantity - payLoadQuantity;
    localStorage.setItem("cartItems", JSON.stringify(state.items));
    return Promise.resolve();
  } catch (err) {
    return Promise.reject(err);
  }
}
export function deleteFromCart(state, payload) {
  try {
    const productIndex = state.items.map((item) => item.id).indexOf(payload.id);
    if (productIndex > -1) {
      state.items.splice(productIndex, 1);
      localStorage.setItem("cartItems", JSON.stringify(state.items));
      return Promise.resolve();
    } else {
      console.log("Bad Request");
      return Promise.reject("Bad Request");
    }
  } catch (err) {
    return Promise.reject(err);
  }
}
