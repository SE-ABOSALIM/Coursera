// HOC (Higher Order Component) topic Example
import withAuth from "../Utils/withAuth";

type DashboardProps = {
  className?: string;
  title?: string;
};

const Dashboard = ({ className, title }: DashboardProps) => {
  return (
    <div className={className}>
      <h1>{title}</h1>
    </div>
  );
};

const AuthDash = withAuth(Dashboard);

export default AuthDash;
