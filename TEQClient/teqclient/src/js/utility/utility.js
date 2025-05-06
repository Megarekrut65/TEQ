import { alertBus } from "@/js/utility/alert-bus.js";

const formatErrors = (errorObj) => {
  let messages = [];

  for (const [field, errors] of Object.entries(errorObj)) {
    let fieldName = field.charAt(0).toUpperCase() + field.slice(1);

    let combinedErrors = errors.join(" ");

    messages.push(`${fieldName}: ${combinedErrors}`);
  }

  return messages.join("\n");
};

export const errorToString = (err) => {
  if (typeof err === "object") {
    if ("detail" in err) err = err.detail;
    if (typeof err === "string") return err;

    return formatErrors(err);
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
