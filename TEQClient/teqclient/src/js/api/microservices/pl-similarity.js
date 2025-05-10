import { sendAsync } from "@/js/utility/request.js";
import { GATEWAY } from "@/js/api/microservices/gateway.js";
import { getRequest } from "@/js/api/api.js";

const API = `${GATEWAY}/pl/similarity/`;

export const findScriptSimilarity = (code1, code2) => {
  const request = getRequest("POST", { code1, code2 });

  return sendAsync(API, request);
};
