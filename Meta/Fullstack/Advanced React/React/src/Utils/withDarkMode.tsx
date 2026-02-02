import type { ComponentType } from "react";

const withDarkMode = (Component: ComponentType) => {
  const activateDarkMode = true;
  const styles = "bg-zinc-900 min-h-screen";
  return (props: any) => {
    return activateDarkMode ? (
      <div className={styles}>
        <Component {...props} modeLabel="Dark Mode" />
      </div>
    ) : (
      <Component {...props} modeLabel="Light Mode" />
    );
  };
};

export default withDarkMode;
