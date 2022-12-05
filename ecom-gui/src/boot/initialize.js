import { boot } from "quasar/wrappers";

export default boot(async ({ store, app }) => {
  await store.dispatch("products/fetchLatestProducts");
  await store.dispatch("products/fetchCategories");
});
