import { sendAsync } from "@/js/utility/request.js";
import { GATEWAY } from "@/js/api/microservices/gateway.js";
import { getRequest } from "@/js/api/api.js";

export const testCode = (language, { script, functionStructure, functionType, unittests }) => {
  const request = getRequest("POST", { script, functionStructure, functionType, unittests });

  return sendAsync(`${GATEWAY}/${language}/test/`, request);
};
