export const defaultAnswer = (testId)=>{
  return {
    testId,
    text: "",
    type: "SINGLE",
    allowProportion: false,
    grade: 1,
    choices: defaultChoices()
  };

};

export const defaultChoices = ()=>{
  return  [
    { text: "", isCorrect: true },
    { text: "", isCorrect: false }
  ];
};
