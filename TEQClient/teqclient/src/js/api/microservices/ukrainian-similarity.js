import { sendAsync } from "@/js/utility/request.js";

const API = "http://127.0.0.1:8005/uk/similarity/";

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
