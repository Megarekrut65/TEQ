import { getToken } from "@/js/utility/token.js";

export const API = import.meta.env.VITE_SERVER_URL;

export const getRequest = (method, body = null, requireToken = false) => {
  const headers = {
    "Content-Type": "application/json",
  };

  if (requireToken) {
    headers["Authorization"] = `Token ${getToken()}`;
  }

  const request = {
    method,
    headers,
  };

  if (body) {
    request["body"] = JSON.stringify(body);
  }

  return request;
};
