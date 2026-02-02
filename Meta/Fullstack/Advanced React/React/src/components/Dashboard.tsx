// HOC (Higher Order Component) topic Example
import withAuth from "../Utils/withAuth";
import withDarkMode from "../Utils/withDarkMode";

type DashboardProps = {
  className?: string;
  title?: string;
  modeLabel: string;
};

const Dashboard = ({ className, title, modeLabel }: DashboardProps) => {
  return (
    <div className={className}>
      <h1>{title}</h1>
      <h1>{modeLabel}</h1>
    </div>
  );
};

const AuthDash = withDarkMode(withAuth(Dashboard));

export default AuthDash;
