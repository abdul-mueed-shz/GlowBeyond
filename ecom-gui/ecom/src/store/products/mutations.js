/*
export function someMutation (state) {
}
*/
export function setLatestProducts(state, payload) {
  state.latestProducts = payload;
}
export function setCategories(state, payload) {
  state.categories = payload;
}
export function setSelectedProduct(state, payload) {
  state.selectedProduct = payload;
}
