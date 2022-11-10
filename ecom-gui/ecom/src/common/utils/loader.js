import { Loading, QSpinnerGears } from "quasar";

export const loader = {
  showLoading: function () {
    Loading.show({
      spinner: QSpinnerGears,
      spinnerColor: "primary",
      spinnerSize: 140,
      backgroundColor: "grey",
      // message: 'Some important process is in progress. Hang on...',
      // messageColor: 'black'
    });
  },
  closeLoading: function () {
    Loading.hide();
  },
};
