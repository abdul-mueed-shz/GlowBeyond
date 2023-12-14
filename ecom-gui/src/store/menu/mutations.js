export function setSelectedMenuItem(state, payload) {
  state.selectedItem = payload;
}
export function addItemToMenu(state, payload) {
  state.menu.push(payload);
}
