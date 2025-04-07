export const defaultAnswer = (testId)=>{
  return {
    testId,
    text:"",
    type:"SINGLE",
    choices:
      [
        { text: "", isCorrect: true },
        { text: "", isCorrect: false }
      ]};
};
