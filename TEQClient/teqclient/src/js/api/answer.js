import { sendAsync } from "@/js/utility/request.js";
import { API, getRequest } from "@/js/api/api.js";

export const testPassGetApi = (testId) => {
  const request = getRequest("GET", null, true);

  return sendAsync(API + `test/${testId}/view`, request);
};

export const testPassPostApi = (testId, { items }) => {
  const request = getRequest("POST", { items }, true);

  return sendAsync(API + `test/${testId}/pass`, request);
};

export const answerGetApi = (answerId) => {
  const request = getRequest("GET", null, true);

  return sendAsync(API + `answer/${answerId}`, request);
};

export const answerLastGetApi = (testId) => {
  const request = getRequest("GET", null, true);

  return sendAsync(API + `answer/${testId}/last`, request);
};

export const answerGetListApi = (page = 1) => {
  const request = getRequest("GET", null, true);

  return sendAsync(API + `answers/?page=${page}`, request);
};

export const answerTestGetListApi = (testId, page = 1) => {
  const request = getRequest("GET", null, true);

  return sendAsync(API + `answers/test/${testId}/?page=${page}`, request);
};

export const answerItemUpdateApi = (answerId, index, { grade }) => {
  const request = getRequest("PUT", { grade }, true);

  return sendAsync(API + `answer/item/${index}/${answerId}/`, request);
};

export const answerCheckUpdateApi = (answerId) => {
  const request = getRequest("PUT", { checked: true }, true);

  return sendAsync(API + `answer/check/${answerId}/`, request);
};

export const answerAgreeUpdateApi = (answerId) => {
  const request = getRequest("PUT", { agree: true }, true);

  return sendAsync(API + `answer/agree/${answerId}/`, request);
};
