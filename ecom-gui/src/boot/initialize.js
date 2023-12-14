import { boot } from "quasar/wrappers";
import { APP_ROUTES } from "src/common/constants/_routes";

export default boot(async ({ store, app }) => {
  await store.dispatch("products/fetchLatestProducts");
  const res = await store.dispatch("products/fetchCategories");
  const menuCategoryItems = [];
  for (const category of res) {
    menuCategoryItems.push({
      name: category.slug,
      label: category.name,
      link: {
        ...APP_ROUTES.CATEGORY,
        PARAMS: {
          slug: category.slug,
        },
      },
      tooltip: category.name,
      icon: category.icon ?? {},
    });
  }
  store.dispatch("menu/addItemToMenu", menuCategoryItems);
});
