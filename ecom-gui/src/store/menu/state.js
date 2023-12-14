import { APP_ROUTES } from "../../common/constants/_routes";

export default function () {
  return {
    menu: [
      {
        name: APP_ROUTES.HOME.NAME,
        label: "Home",
        link: APP_ROUTES.HOME,
        tooltip: "Home",
        icon: {
          name: "mdi-home",
          size: "",
        },
      },
      // {
      //   name: APP_ROUTES.CATEGORY.NAME,
      //   label: "Summer",
      //   link: APP_ROUTES.CATEGORY.PATH + "/skin-care",
      //   tooltip: "Summer",
      //   icon: {
      //     name: "mdi-white-balance-sunny",
      //     size: "",
      //   },
      // },
      {
        name: APP_ROUTES.CART.NAME,
        label: "Cart",
        link: APP_ROUTES.CART,
        tooltip: "Cart",
        icon: {
          name: "mdi-cart",
          size: "",
        },
      },
    ],
    selectedItem: "home",
  };
}
