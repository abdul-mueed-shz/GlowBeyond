/*
export function someMutation (state) {
}
*/
export function toggleMiniState(state) {
  state.miniState = !state.miniState;
}

export function doctitle(state, payload) {
  document.title = `Stark | ${payload.name}`;
}
