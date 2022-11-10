import { APP_ROUTES } from "../../common/constants/_routes";

export default function () {
  return {
    menu: [
      {
        name: APP_ROUTES.HOME.NAME,
        label: "HOME",
        link: APP_ROUTES.HOME.PATH,
        icon: {
          name: "mdi-home",
          size: "",
        },
      },
      {
        name: APP_ROUTES.SUMMER.NAME,
        label: "Summer",
        link: APP_ROUTES.SUMMER.PATH,
        icon: {
          name: "mdi-book",
          size: "",
        },
      },
      {
        name: APP_ROUTES.WINTER.NAME,
        label: "Winter",
        link: APP_ROUTES.WINTER.PATH,
        icon: {
          name: "mdi-mail",
          size: "",
        },
      },
      {
        name: APP_ROUTES.CART.NAME,
        label: "Cart",
        link: APP_ROUTES.CART.PATH,
        icon: {
          name: "mdi-cart",
          size: "",
        },
      },
    ],
    selectedItem: "home",
  };
}
