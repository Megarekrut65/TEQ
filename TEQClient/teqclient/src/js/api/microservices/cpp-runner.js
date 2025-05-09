import { sendAsync } from "@/js/utility/request.js";
import { GATEWAY } from "@/js/api/microservices/gateway.js";

const API = `${GATEWAY}/cpp/run/`;

export const runCppCode = (script) => {
  const request = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ script }),
  };

  return sendAsync(API, request);
};
