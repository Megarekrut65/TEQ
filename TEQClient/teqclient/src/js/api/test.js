import { sendAsync } from "@/js/utility/request.js";
import { API, getRequest } from "@/js/api/api.js";

export const testCreateApi = ({ title, description, category }) => {
  const request = getRequest("POST", { title, description, category }, true);

  return sendAsync(API + "test/", request);
};

const testGetDeleteApi = (testId, method) => {
  const request = getRequest(method, null, true);
  return sendAsync(API + `test/${testId}/`, request);
};

export const testGetApi = (testId) => {
  return testGetDeleteApi(testId, "GET");
};

export const testDeleteApi = (testId) => {
  return testGetDeleteApi(testId, "DELETE");
};

export const testUpdateApi = (
  testId,
  { title, description, category, isPublic, canShare, autoCheck, showResult, showCorrect },
) => {
  const request = getRequest(
    "PUT",
    {
      title,
      description,
      category,
      isPublic,
      canShare,
      autoCheck,
      showResult,
      showCorrect,
    },
    true,
  );

  return sendAsync(API + `test/${testId}/`, request);
};

export const testListApi = () => {
  const request = getRequest("GET", null, true);

  return sendAsync(API + `tests/`, request);
};

export const publicTestListApi = (category) => {
  const request = getRequest("GET");

  return sendAsync(API + `public/tests/${category ? "?category=" + category : ""}`, request);
};
