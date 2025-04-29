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
    },
    {
        ace: "C_Cpp",
        name: "C++",
        type: "cpp",
        runner: runCppCode,
        script: '#include <iostream>\n\nint main() {\n\tstd::cout<<"Hello world";\n\treturn 0;\n}',
    },
    {
        ace: "java",
        name: "Java",
        type: "java",
        runner: runJavaCode,
        script: 'public class Script { \n\tpublic static void main(String[] args) { \n\t\tSystem.out.println("Hello World");\n\t}\n}',
    },
];

export const getLanguage=(type)=>{
  return languages.find(lang => lang.type === type);
};
