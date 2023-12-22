import { api } from "src/boot/axios";

export async function setSocials({ commit }) {
  try {
    const res = await api.get("socials");
    commit("setSocials", res.data);
    return res.data;
  } catch (err) {
    throw new Error(err);
  }
}

export async function setAppInfo({ commit }) {
  try {
    const res = await api.get("app-info");
    if (res.data[0]) {
      commit("setAppInfo", res.data[0]);
    }
    return res.data;
  } catch (err) {
    throw new Error(err);
  }
}
