import { runPythonCode } from "@/js/api/microservices/python-runner.js";
import { runCppCode } from "@/js/api/microservices/cpp-runner.js";
import { runJavaCode } from "@/js/api/microservices/java-runner.js";

export const languages = [
  {
    ace: "python",
    name: "Python",
    runner: runPythonCode,
    type: "python",
    script: "print('Hello world')",
    testFunStruct: "def concat(text1:str, text2:str)->str",
    testFun: "def concat(text1:str, text2:str)->str:\n\tpass # write your code here",
  },
  {
    ace: "C_Cpp",
    name: "C++",
    type: "cpp",
    runner: runCppCode,
    script: '#include <iostream>\n\nint main() {\n\tstd::cout<<"Hello world";\n\treturn 0;\n}',
    testFunStruct: "std::string concat(std::string text1, std::string text2)",
    testFun:
      "std::string concat(std::string text1, std::string text2){\n\t//write your code here\n}",
  },
  {
    ace: "java",
    name: "Java",
    type: "java",
    runner: runJavaCode,
    script:
      'public class Script { \n\tpublic static void main(String[] args) { \n\t\tSystem.out.println("Hello World");\n\t}\n}',
    testFunStruct: "String concat(String text1, String text2)",
    testFun:
      "public class Solution {\n\tString concat(String text1, String text2) {\n\t\t//write your code here\n\t}\n}",
  },
];

export const getLanguage = (type) => {
  return languages.find((lang) => lang.type === type);
};
