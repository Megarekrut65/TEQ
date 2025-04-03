import { sendAsync } from "@/js/utility/request.js";
import { API } from "@/js/api/api.js";
import { getToken } from "@/js/utility/token.js";

export const itemCreateApi = ({ testId, text, type, choices, correct_answer }) => {
  const request = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    },
    body: JSON.stringify({ testId, text, type, choices, correct_answer })
  };
  return sendAsync(API + "test/item/", request);
};
/*
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

export const testUpdateApi = (testId, { title, description, isPublic }) => {
  const request = {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    },
    body: JSON.stringify({ title, description, isPublic })
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
};*/
