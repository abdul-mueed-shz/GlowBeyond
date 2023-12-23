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

export async function setMailingInfo({ commit }) {
  try {
    const res = await api.get("mailing-info");
    commit("setMailingInfo", res.data);
    return res.data;
  } catch (err) {
    throw new Error(err);
  }
}

export async function setContactInfo({ commit }) {
  try {
    const res = await api.get("contact-info");
    commit("setContactInfo", res.data);
    return res.data;
  } catch (err) {
    throw new Error(err);
  }
}

export async function setBannerItems({ commit }) {
  try {
    const res = await api.get("banner-items");
    commit("setBannerItems", res.data);
    return res.data;
  } catch (err) {
    throw new Error(err);
  }
}

export async function setBannerNotification({ commit }) {
  try {
    const res = await api.get("banner-notification");
    if (res.data.length) {
      commit("setBannerNotification", res.data[0]);
    }
    return res.data;
  } catch (err) {
    throw new Error(err);
  }
}
