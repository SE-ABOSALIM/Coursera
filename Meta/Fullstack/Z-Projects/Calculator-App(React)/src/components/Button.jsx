import { useState } from "react";

const Button = () => {
  return (
    <div>
      <button
        onClick={() => setInput(symbol)}
        className={`button ${className || ""}`}
      >
        {symbol}
      </button>
    </div>
  );
};

export default Button;
