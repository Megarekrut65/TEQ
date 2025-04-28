import { runPythonCode } from "@/js/api/microservices/python-runner.js";

export const languages = [
    { ace: "python", name: "Python", runner:runPythonCode, type:"python" },
    { ace: "C_Cpp", name: "C++", type:"cpp" },
];
