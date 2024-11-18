import { alertBus } from "@/js/utility/alert-bus.js";

export const errorToString = (err) => {
  if (typeof err === "object" && "detail" in err) {
    const detail = err.detail;
    if (typeof detail === "string") return detail;

    let res = "";
    detail.forEach((error) => {
      res += error + " ";
    });

    return res;
  }

  return err;
};

export const errorAlert = (err) => {
  alertBus.addAlert(errorToString(err), "danger", 0);
};
