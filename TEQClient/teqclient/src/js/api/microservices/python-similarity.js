import { sendAsync } from "@/js/utility/request.js";

const API = "http://127.0.0.1:8006/python/similarity/";

export const findPythonSimilarity = (code1, code2) => {
  const request = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ code1, code2 }),
  };

  return sendAsync(API, request);
};
