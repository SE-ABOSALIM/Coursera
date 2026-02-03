/* Render Props Currency converter app example */
import { useState } from "react";

type renderFunc = {
  render: (amount: number) => React.ReactNode;
};

const CCApp = ({ render }: renderFunc) => {
  const [amount, setAmount] = useState<number>(0);

  const handleAmount = (e: React.ChangeEvent<HTMLInputElement>) => {
    setAmount(Number(e.target.value));
  };

  return (
    <>
      <div className="flex flex-col gap-2 m-5">
        <label>Amount:</label>
        <input
          type="text"
          placeholder="Enter Amount(TL)"
          className="w-52 p-[2px] border-black border-2 rounded-lg"
          onChange={handleAmount}
          value={amount}
        />
      </div>

      <div>{render(amount)}</div>
    </>
  );
};

export default CCApp;
