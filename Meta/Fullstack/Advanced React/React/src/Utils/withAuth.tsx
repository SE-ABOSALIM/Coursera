// HOC (Higher Order Component) topic Example
import type { ComponentType } from "react";

const withAuth = (Component: ComponentType<any>) => {
  const isAuth = false;
  return (props: any) => {
    if (isAuth) {
      return <Component {...props} />;
    } else {
      return <p>Please login to access</p>;
    }
  };
};

export default withAuth;
