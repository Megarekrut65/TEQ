import { languages } from "@/js/languages.js";

export const defaultAnswer = () => {
  return {
    text: "",
    type: "SINGLE",
    allowProportion: false,
    grade: 1,
    choices: defaultChoices(),
    minSimilarPercent: 100,
    language: languages[0].type,
  };
};

export const defaultChoices = () => {
  return [
    { text: "", isCorrect: true },
    { text: "", isCorrect: false },
  ];
};

export const defaultUnitTest = (index) => {
  return {
    name: `unittest_${index}`,
    in_test: '"Hello", "World"',
    out_test: '"Hello World"',
    type: "string",
  };
};

export const defaultUnitTests = (index) => {
  return [defaultUnitTest(index)];
};
