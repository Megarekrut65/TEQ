
import { sendAsync } from "@/js/utility/request.js";

const API = "http://127.0.0.1:8007/cpp/run/"

export const runCppCode = (script) =>{
  const request = {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({script})
  };

  return sendAsync(API, request);
};
