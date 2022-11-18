import { boot } from "quasar/wrappers";

export default boot(async ({ store, router }) => {
  await store.dispatch("cart/initializeCart");
  await store.dispatch("products/fetchLatestProducts");
  await store.dispatch("products/fetchCategories");
});
