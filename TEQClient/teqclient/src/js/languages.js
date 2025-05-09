export const languages = [
  {
    ace: "python",
    name: "Python",
    type: "python",
    script: "print('Hello world')",
    testFunStruct: "def concat(text1:str, text2:str)->str",
    testFun: "def concat(text1:str, text2:str)->str:\n\tpass # write your code here",
  },
  {
    ace: "C_Cpp",
    name: "C++",
    type: "cpp",
    script: '#include <iostream>\n\nint main() {\n\tstd::cout<<"Hello world";\n\treturn 0;\n}',
    testFunStruct: "std::string concat(std::string text1, std::string text2)",
    testFun:
      "#include <string>\n\nstd::string concat(std::string text1, std::string text2){\n\t//write your code here\n}",
  },
  {
    ace: "java",
    name: "Java",
    type: "java",
    script:
      'public class Script { \n\tpublic static void main(String[] args) { \n\t\tSystem.out.println("Hello World");\n\t}\n}',
    testFunStruct: "public static String concat(String text1, String text2)",
    testFun:
      "class Solution {\n\tpublic static String concat(String text1, String text2) {\n\t\t//write your code here\n\t}\n}",
  },
];

export const getLanguage = (type) => {
  return languages.find((lang) => lang.type === type);
};

export const isDefaultScript = (script) => {
  for (let lang of languages) {
    if (lang.script === script || lang.testFun === script) return true;
  }

  return (script?.trim() ?? "") === "";
};

export const isDefaultStructure = (structure) => {
  for (let lang of languages) {
    if (lang.testFunStruct === structure) return true;
  }

  return (structure?.trim() ?? "") === "";
};
