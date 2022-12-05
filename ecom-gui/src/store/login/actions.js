import { api } from "src/boot/axios";

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
