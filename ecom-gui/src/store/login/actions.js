import { api } from "src/boot/axios";

let id;

export async function getAuthDetails({ commit }, queryParams) {
  try {
    const url = "set_auth_details";
    const authDetails = await api.get(url, { params: queryParams });
    commit("setLoginDetails", authDetails.data);
    return authDetails.data;
  } catch (err) {
    console.log(err);
  }
}
export async function callLogout({ commit }) {
  try {
    const url = "logout";
    const result = await api.post(url);
    clearTimeout(id);
    return result.data;
  } catch (err) {
    console.log(err);
  }
}

export function setLoginDetails({ commit }, payload) {
  commit("setLoginDetails", payload);
}
export function setIntervalId({ commit }, payload) {
  commit("setIntervalId", payload);
}
