type PoundProps = {
  amount: number;
};

const POUND = ({ amount }: PoundProps) => {
  return <div className="ml-4">POUND: {(amount * 0.017).toFixed(2)}</div>;
};

export default POUND;
