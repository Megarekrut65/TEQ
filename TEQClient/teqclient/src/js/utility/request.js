/**
 *
 * @param {string} endpoint - path to server request
 * @param {Object} request - request to send it to server
 * @returns promise to server answer data or error
 */
export const sendAsync = async (endpoint, request) => {
  const response = await fetch(endpoint, request);

  if (!response.ok) {
    return response
      .text()
      .then((err) => {
        try{
          err = JSON.parse(err);
          // eslint-disable-next-line no-unused-vars
        } catch (e) { /* empty */ }

        throw err;
      });
  }
  if (response.statusText === "No Content") return response.text();
  return response.json();
};
