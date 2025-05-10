import { sendAsync } from "@/js/utility/request.js";
import { API, getRequest } from "@/js/api/api.js";

export const itemCreateApi = (
  containerId,
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
  endpoint = "test",
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
  const request = getRequest("POST", payload, true);

  return sendAsync(`${API}${endpoint}/item/${containerId}/`, request);
};

export const itemDeleteApi = (containerId, index, endpoint = "test") => {
  const request = getRequest("DELETE", null, true);

  return sendAsync(API + `${endpoint}/item/${index}/${containerId}/`, request);
};

export const itemUpdateApi = (
  containerId,
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
  endpoint = "test",
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

  const request = getRequest("PUT", payload, true);

  return sendAsync(API + `${endpoint}/item/${index}/${containerId}/`, request);
};
