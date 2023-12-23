export function setCartQuantity(state, quantity) {
  state.cartQuantity = quantity;
}
export function addToCart(state, payload) {
  try {
    const product = state.items.find((item) => item.id === payload.id);
    if (product) {
      product.quantity =
        parseInt(product.quantity ?? 0) + parseInt(payload.quantity);
    } else {
      state.items.push(payload);
    }
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
      return Promise.resolve();
    }
    if (payLoadQuantity < 0 || payLoadQuantity > productQuantity) {
      console.log("Bad Request");
      return Promise.reject("Bad Request");
    }
    state.items[productIndex].quantity = productQuantity - payLoadQuantity;
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
      return Promise.resolve();
    } else {
      throw new Error("Bad Request");
    }
  } catch (err) {
    return Promise.reject(err);
  }
}

export async function clearCart(state) {
  state.items = [];
  state.cartQuantity = 0;
}
