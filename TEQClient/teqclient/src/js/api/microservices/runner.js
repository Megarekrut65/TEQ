import { sendAsync } from "@/js/utility/request.js";
import { GATEWAY } from "@/js/api/microservices/gateway.js";
import { getRequest } from "@/js/api/api.js";

export const runCode = (language, script) => {
  const request = getRequest("POST", { script });

  return sendAsync(`${GATEWAY}/${language}/run/`, request);
};
