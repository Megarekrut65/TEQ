import { sendAsync } from "@/js/utility/request.js";
import { GATEWAY } from "@/js/api/microservices/gateway.js";
import { getRequest } from "@/js/api/api.js";

const API = `${GATEWAY}/nl/similarity/`;

export const findTextSimilarity = (text1, text2) => {
  const request = getRequest("POST", { text1, text2 });
  return sendAsync(API, request);
};
