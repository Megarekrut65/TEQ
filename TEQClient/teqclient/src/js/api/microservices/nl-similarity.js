import { sendAsync } from "@/js/utility/request.js";
import { GATEWAY } from "@/js/api/microservices/gateway.js";

const API = `${GATEWAY}/nl/similarity/`;

export const findTextSimilarity = (text1, text2) => {
  const request = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text1, text2 }),
  };

  return sendAsync(API, request);
};
