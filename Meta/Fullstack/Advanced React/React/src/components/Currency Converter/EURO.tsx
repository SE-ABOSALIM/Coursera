/* Render Props Currency converter app example */
type EuroProps = {
  amount: number;
};

const EURO = ({ amount }: EuroProps) => {
  return <div className="ml-4">EURO: {(amount * 0.019).toFixed(2)}</div>;
};

export default EURO;
