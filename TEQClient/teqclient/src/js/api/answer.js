import { getToken } from "@/js/utility/token.js";
import { sendAsync } from "@/js/utility/request.js";
import { API } from "@/js/api/api.js";

export const testViewGetApi = (testId) => {
  const request = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    }
  };
  return sendAsync(API + `test/${testId}/view`, request);
};
