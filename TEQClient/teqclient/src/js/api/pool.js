import { sendAsync } from "@/js/utility/request.js";
import { API, getRequest } from "@/js/api/api.js";

export const poolGetApi = () => {
  const request = getRequest("GET", null, true);

  return sendAsync(API + `pool/`, request);
};

export const categoryCreateApi = ({ name }) => {
  const request = getRequest("POST", { name }, true);

  return sendAsync(API + "category/", request);
};

export const categoryGetApi = (categoryId) => {
  const request = getRequest("GET", null, true);

  return sendAsync(API + `category/${categoryId}/`, request);
};

export const categoryDeleteApi = (categoryId) => {
  const request = getRequest("DELETE", null, true);

  return sendAsync(API + `category/${categoryId}/`, request);
};

export const categoryUpdateApi = (categoryId, { name }) => {
  const request = getRequest("PUT", { name }, true);

  return sendAsync(API + `category/${categoryId}/`, request);
};
