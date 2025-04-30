import { sendAsync } from "@/js/utility/request.js";

const API = "http://127.0.0.1:8016/python/test/";

export const testPythonCode = ({ script, functionStructure, functionType, unittests }) => {
  const request = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ script, functionStructure, functionType, unittests }),
  };
  console.log({ script, functionStructure, functionType, unittests });
  return sendAsync(API, request);
};
