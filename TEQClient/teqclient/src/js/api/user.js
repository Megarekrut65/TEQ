import { sendAsync } from "@/js/utility/request.js";
import { API, getRequest } from "@/js/api/api.js";

export const loginApi = ({ email, password }) => {
  const request = getRequest("POST", { email, password });

  return sendAsync(API + "login/", request);
};

export const registerApi = ({ fullname, email, password }) => {
  const request = getRequest("POST", { fullname, email, password });

  return sendAsync(API + "register/", request);
};
