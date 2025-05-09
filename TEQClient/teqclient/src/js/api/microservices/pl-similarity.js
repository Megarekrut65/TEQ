import { sendAsync } from "@/js/utility/request.js";
import { GATEWAY } from "@/js/api/microservices/gateway.js";

const API = `${GATEWAY}/pl/similarity/`;

export const findScriptSimilarity = (code1, code2) => {
  const request = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ code1, code2 }),
  };

  return sendAsync(API, request);
};
