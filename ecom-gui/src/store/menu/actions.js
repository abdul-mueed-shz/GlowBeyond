export function addItemToMenu({ commit }, payload = []) {
  for (const item of payload) {
    commit("addItemToMenu", item);
  }
}

export function setSelectedMenuItem({ commit }, name) {
  commit("setSelectedMenuItem", name);
}
