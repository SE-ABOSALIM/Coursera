import { useState } from "react";

const App = () => {
  const operators = ["+", "-", "x", "÷"];
  const [input, setInput] = useState("");
  const [result, setResult] = useState("");

  const handleInput = (val) => {
    const last = input.slice(-1);

    if (operators.includes(last) && operators.includes(val)) return;
    setInput((prev) => prev.toString() + val.toString());
  };

  const calculate = () => {
    if (!input) return;
    if (
      input.endsWith("+") ||
      input.endsWith("-") ||
      input.endsWith("x") ||
      input.endsWith("÷")
    ) {
      setResult("Syntax Error");
      return;
    }

    const expression = input.replace(/÷/g, "/").replace(/x/g, "*");

    try {
      let result = Function(`"use strict"; return (${expression})`)();
      result = Number(result.toFixed(5));
      setResult(result.toString());
    } catch {
      setInput("Error");
    }
  };

  const deleteLast = () => {
    setInput((prev) => prev.slice(0, -1));
  };

  const clearInput = () => {
    setInput("");
    setResult("");
  };

  return (
    <div className="bg-slate-500 w-[310px] h-[450px] rounded-xl border-black border-[3px] p-2">
      <div className="flex justify-center items-center">
        <div className="relative flex items-center justify-end bg-amber-500 w-[300px] h-28 mt-2 rounded-xl">
          <div className="flex flex-col justify-end items-end gap-[18px] mx-4 mt-2">
            <div className="text-gray-800">{input}</div>
            <output className="text-[23px]">{result}</output>
          </div>
          <button
            className="absolute left-[10px] bottom-2 font-serif text-2xl"
            onClick={clearInput}
          >
            <i className="fa-solid fa-c"></i>
          </button>
          <button
            className="absolute left-2 top-2 font-serif text-xl"
            onClick={deleteLast}
          >
            <i className="fa-solid fa-delete-left"></i>
          </button>
        </div>
      </div>
      <div className="flex justify-between items-end p-2">
        <div className="grid grid-cols-3 w-48 gap-5 pt-2">
          <button className="button" onClick={() => handleInput(1)}>
            <i className="fa-solid fa-1"></i>
          </button>
          <button className="button" onClick={() => handleInput(2)}>
            <i className="fa-solid fa-2"></i>
          </button>
          <button className="button" onClick={() => handleInput(3)}>
            <i className="fa-solid fa-3"></i>
          </button>
          <button className="button" onClick={() => handleInput(4)}>
            <i className="fa-solid fa-4"></i>
          </button>
          <button className="button" onClick={() => handleInput(5)}>
            <i className="fa-solid fa-5"></i>
          </button>
          <button className="button" onClick={() => handleInput(6)}>
            <i className="fa-solid fa-6"></i>
          </button>
          <button className="button" onClick={() => handleInput(7)}>
            <i className="fa-solid fa-7"></i>
          </button>
          <button className="button" onClick={() => handleInput(8)}>
            <i className="fa-solid fa-8"></i>
          </button>
          <button className="button" onClick={() => handleInput(9)}>
            <i className="fa-solid fa-9"></i>
          </button>
          <button className="button" onClick={() => handleInput(".")}>
            <i className="fa-solid fa-circle text-[5px]"></i>
          </button>
          <button className="button" onClick={() => handleInput(0)}>
            <i className="fa-solid fa-0"></i>
          </button>
          <button className="button" onClick={calculate}>
            <i className="fa-solid fa-equals"></i>
          </button>
        </div>
        <div className="flex flex-col gap-5">
          <button
            className="button w-14 text-xl"
            onClick={() => handleInput("+")}
          >
            <i className="fa-solid fa-plus"></i>
          </button>
          <button
            className="button w-14 text-xl"
            onClick={() => handleInput("-")}
          >
            <i className="fa-solid fa-minus"></i>
          </button>
          <button
            className="button w-14 text-xl"
            onClick={() => handleInput("x")}
          >
            <i className="fa-solid fa-xmark"></i>
          </button>
          <button
            className="button w-14 text-xl"
            onClick={() => {
              handleInput("÷");
            }}
          >
            <i className="fa-solid fa-divide"></i>
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;
