import {
  FULL,
  MULTIPLE,
  RETURN_TYPES,
  SCRIPT,
  SCRIPT_UNITTEST,
  SHORT,
  SINGLE,
} from "@/js/types.js";
import { defaultChoices, defaultUnitTests } from "@/js/data-types.js";
import { getLanguage, languages } from "@/js/languages.js";

export const formatItem = (item) => {
  if (
    [SINGLE, MULTIPLE].includes(item.type) &&
    (item.choices == null || item.choices.length === 0)
  ) {
    item.choices = defaultChoices();
  }

  if ([SCRIPT].includes(item.type) && !item.language) {
    item.language = languages[0].type;
  }

  if ([SCRIPT, SHORT, FULL].includes(item.type) && !item.minSimilarPercent) {
    item.minSimilarPercent = 99;
  }

  if ([SCRIPT].includes(item.type) && !item.language) {
    item.language = languages[0].type;
  }

  if ([SCRIPT_UNITTEST].includes(item.type)) {
    if (!item.language) item.language = languages[0].type;
    if (!item.publicUnittests || !item.privateUnittests) {
      item.privateUnittests = defaultUnitTests(1);
      item.publicUnittests = defaultUnitTests(1);
      const lang = getLanguage(item.language);
      item.correctAnswer = lang.testFun;
      item.functionStructure = lang.testFunStruct;
      item.functionType = RETURN_TYPES[0];
    }
    if (item.functionStructure === "") item.functionStructure = "_";
  }
};
