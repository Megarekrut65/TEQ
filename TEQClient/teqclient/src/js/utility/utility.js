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
  console.log(err);
  alertBus.addAlert(errorToString(err), "danger", 0);
};

export const successAlert = (text) => {
  alertBus.addAlert(text, "success", 5);
};

export const truncate = (str, length = 20) =>
  str && str.length > length ? str.slice(0, length) + "..." : str;

export const copyToClipboard = (text) => {
  return navigator.clipboard.writeText(text);
};

export const extractNumber = (text) => {
  return text.match(/\d+(\.\d+)?/g).map(Number)[0];
};
