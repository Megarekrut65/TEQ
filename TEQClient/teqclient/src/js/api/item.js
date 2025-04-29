import { sendAsync } from "@/js/utility/request.js";
import { API } from "@/js/api/api.js";
import { getToken } from "@/js/utility/token.js";

export const itemCreateApi = (
  testId,
  {
    text,
    type,
    grade,
    allowProportion = false,
    choices = [],
    correctAnswer = null,
    minSimilarPercent = 0,
    language = null,
    publicUnittests = [],
    privateUnittests = [],
    functionStructure = null,
    functionType = null,
  },
) => {
  const payload = {
    text,
    type,
    grade,
    allowProportion,
    choices,
    correctAnswer,
    minSimilarPercent,
    language,
    publicUnittests,
    privateUnittests,
    functionStructure,
    functionType,
  };

  const request = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`,
    },
    body: JSON.stringify(payload),
  };

  return sendAsync(`${API}item/${testId}/`, request);
};

export const itemDeleteApi = (testId, index) => {
  const request = {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`,
    },
  };
  return sendAsync(API + `item/${index}/${testId}/`, request);
};

export const itemUpdateApi = (
  testId,
  index,
  {
    text,
    type,
    grade,
    allowProportion = false,
    choices = [],
    correctAnswer = null,
    minSimilarPercent = 0,
    language = null,
    publicUnittests = [],
    privateUnittests = [],
    functionStructure = null,
    functionType = null,
  },
) => {
  const payload = {
    text,
    type,
    grade,
    allowProportion,
    choices,
    correctAnswer,
    minSimilarPercent,
    language,
    publicUnittests,
    privateUnittests,
    functionStructure,
    functionType,
  };

  const request = {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${getToken()}`,
    },
    body: JSON.stringify(payload),
  };

  return sendAsync(API + `item/${index}/${testId}/`, request);
};
