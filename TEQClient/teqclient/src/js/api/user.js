import { sendAsync } from "@/js/utility/request.js";
import { API } from "@/js/api/api.js";

export const loginApi = ({ email, password }) => {
    const request = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
    };
    return sendAsync(API + "login/", request);
};

export const registerApi = ({ fullname, email, password }) => {
    const request = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ fullname, email, password }),
    };
    return sendAsync(API + "register/", request);
};
