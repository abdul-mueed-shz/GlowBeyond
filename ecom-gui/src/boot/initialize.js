import { boot } from "quasar/wrappers";

export default boot(async ({ store }) => {
  await store.dispatch("cart/initializeCart");
  await store.dispatch("products/fetchLatestProducts");
  await store.dispatch("products/fetchCategories");
});
