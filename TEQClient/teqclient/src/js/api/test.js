import { sendAsync } from "@/js/utility/request.js";
import { API } from "@/js/api/api.js";
import { getToken } from "@/js/utility/token.js";

export const testCreateApi = ({ title, description, isPublic }) => {
  const request = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    },
    body: JSON.stringify({ title, description, isPublic })
  };
  return sendAsync(API + "test/", request);
};

const testGetDeleteApi = (testId, method) => {
  const request = {
    method: method,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    }
  };
  return sendAsync(API + `test/${testId}/`, request);
};

export const testGetApi = (testId) => {
  return testGetDeleteApi(testId, "GET");
};

export const testDeleteApi = (testId) => {
  return testGetDeleteApi(testId, "DELETE");
};

export const testUpdateApi = (testId, { title, description, isPublic, autoCheck, showResult, showCorrect }) => {
  const request = {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    },
    body: JSON.stringify({ title, description, isPublic,  autoCheck, showResult, showCorrect })
  };

  return sendAsync(API + `test/${testId}/`, request);
};

export const testListApi = () => {
  const request = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    }
  };

  return sendAsync(API + `tests/`, request);
};
