/* Render Props Currency converter app example */
type USDProps = {
  amount: number;
};

const USD = ({ amount }: USDProps) => {
  return <div className="ml-4">USD: {(amount * 0.023).toFixed(2)}</div>;
};

export default USD;
