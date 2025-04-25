export const copyObject = (key, obj) => {
  localStorage.setItem(`clipboard-${key}`, JSON.stringify(obj))
};

export const pasteObject = (key) => {
  try{
    return JSON.parse(localStorage.getItem(`clipboard-${key}`));
  }
    // eslint-disable-next-line no-unused-vars
  catch (err) {
    return null;
  }
};
