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

export const successAlert = (err) => {
    alertBus.addAlert(errorToString(err), "success", 5);
};

export const truncate = (str, length = 20) =>
    str && str.length > length ? str.slice(0, length) + "..." : str;

export const copyToClipboard = (text) => {
    return navigator.clipboard.writeText(text);
};
