import { sendAsync } from "@/js/utility/request.js";
import { GATEWAY } from "@/js/api/microservices/gateway.js";

export const testCode = (language, { script, functionStructure, functionType, unittests }) => {
  const request = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ script, functionStructure, functionType, unittests }),
  };
  console.log({ script, functionStructure, functionType, unittests });
  return sendAsync(`${GATEWAY}/${language}/test/`, request);
};
