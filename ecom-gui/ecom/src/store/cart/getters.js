export function getCartUniqueQuantity(state) {
  return state.cartQuantity;
}
export function getCartQuantity(state) {
  let totalQuantity = 0;
  state.items.forEach((item) => {
    totalQuantity += item.quantity;
  });
  return totalQuantity;
}
export function getCartItems(state) {
  return state.items;
}
export function getCartTotal(state) {
  let totalCartPrice = 0;
  state.items.forEach((item) => {
    totalCartPrice += item.price * item.quantity;
  });
  return totalCartPrice;
}
export function getCartItemTotal(state) {
  return (id) => {
    const product = state.items.find((item) => item.id === id);
    if (product) {
      return product.quantity * product.price;
    }
    return `No item with id ${id} found`;
  };
}
