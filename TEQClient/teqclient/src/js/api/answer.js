import { getToken } from "@/js/utility/token.js";
import { sendAsync } from "@/js/utility/request.js";
import { API } from "@/js/api/api.js";

export const testPassGetApi = (testId) => {
  const request = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    }
  };
  return sendAsync(API + `test/${testId}/view`, request);
};

export const testPassPostApi = (testId, { items }) => {
    const request = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${getToken()}`,
        },
        body: JSON.stringify({ items }),
    };
    return sendAsync(API + `test/${testId}/pass`, request);
};

export const answerGetApi = (answerId) => {
  const request = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    }
  };
  return sendAsync(API + `answer/${answerId}`, request);
};

export const answerLastGetApi = (testId) => {
  const request = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    }
  };
  return sendAsync(API + `answer/${testId}/last`, request);
};

export const answerGetListApi = (page=1) => {
  const request = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    }
  };
  return sendAsync(API + `answers/?page=${page}`, request);
};

export const answerTestGetListApi = (testId, page=1) => {
  const request = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    }
  };
  return sendAsync(API + `answers/test/${testId}/?page=${page}`, request);
};

export const answerItemUpdateApi = (answerId, index, { grade  }) => {
  const request = {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    },
    body: JSON.stringify({grade  })
  };

  return sendAsync(API + `answer/item/${index}/${answerId}/`, request);
};

export const answerCheckUpdateApi = (answerId) => {
  const request = {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    },
    body: JSON.stringify({checked:true})
  };

  return sendAsync(API + `answer/check/${answerId}/`, request);
};
