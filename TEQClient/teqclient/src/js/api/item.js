import { sendAsync } from "@/js/utility/request.js";
import { API } from "@/js/api/api.js";
import { getToken } from "@/js/utility/token.js";

export const itemCreateApi = ({ testId, text, type, choices, grade, allowProportion,
                                correctAnswer=null, minSimilarPercent=0 }) => {
  const request = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    },
    body: JSON.stringify({ testId, text, type, choices, correctAnswer, grade, allowProportion, minSimilarPercent })
  };

  return sendAsync(API + "item/", request);
};

export const itemDeleteApi = (testId, index) => {
  const request = {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    }
  };
  return sendAsync(API + `item/${index}/${testId}/`, request);
};


export const itemUpdateApi = (testId, index, { text, type, choices,grade, allowProportion,
    correctAnswer=null, minSimilarPercent=0  }) => {
  const request = {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`
    },
    body: JSON.stringify({testId, text, type, choices,  correctAnswer, grade, allowProportion, minSimilarPercent  })
  };

  return sendAsync(API + `item/${index}/${testId}/`, request);
};


