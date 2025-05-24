import { languages } from "@/js/languages.js";
import {SINGLE} from "@/js/types.js";

export const defaultAnswer = (type=SINGLE) => {
  return {
    text: "",
    type: type,
    allowProportion: false,
    grade: 1,
    choices: defaultChoices(),
    minSimilarPercent: 90,
    language: languages[0].type,
  };
};

export const defaultChoices = () => {
  return [
    { text: "", isCorrect: true },
    { text: "", isCorrect: false },
  ];
};

export const defaultUnitTest = (prefix) => {
  return {
    inTest: '"Hello", "World"',
    outTest: '"Hello World"',
    prefix: prefix,
  };
};

export const defaultUnitTests = (prefix) => {
  return [defaultUnitTest(prefix)];
};
