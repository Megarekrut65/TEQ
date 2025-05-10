import { sendAsync } from "@/js/utility/request.js";
import { API, getRequest } from "@/js/api/api.js";

export const memberCreateApi = (testId, { emails }) => {
  const request = getRequest("POST", { emails }, true);

  return sendAsync(API + `member/${testId}/add`, request);
};

export const memberListApi = (testId) => {
  const request = getRequest("GET", null, true);
  return sendAsync(API + `members/${testId}`, request);
};

export const memberDeleteApi = (memberId) => {
  const request = getRequest("DELETE", null, true);

  return sendAsync(API + `member/${memberId}`, request);
};
