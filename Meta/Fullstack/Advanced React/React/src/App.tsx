const App = () => {
  return <></>;
};

export default App;

/* Render Props Currency converter app example */
// import CCApp from "./components/Currency Converter/CCApp";
// import EURO from "./components/Currency Converter/EURO";
// import POUND from "./components/Currency Converter/POUND";
// import USD from "./components/Currency Converter/USD";

// const App = () => {
//   return (
//     <>
//       <CCApp
//         render={(amount: number) => {
//           return (
//             <>
//               <USD amount={amount} />
//               <EURO amount={amount} />
//               <POUND amount={amount} />
//             </>
//           );
//         }}
//       />
//     </>
//   );
// };

// export default App;

/* Render Props Advanced Example */
// import FormHandler from "./components/FormHandler";

// type FormHandlerRenderArgs = {
//   formData: Record<string, unknown>;
//   error: { msg?: string } | null;
//   handleChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
//   handleSubmit: (e: React.FormEvent<HTMLFormElement>) => void;
// };

// const App = () => {
//   const form = ({
//     formData,
//     error,
//     handleChange,
//     handleSubmit,
//   }: FormHandlerRenderArgs) => {
//     return (
//       <>
//         <form onSubmit={handleSubmit}>
//           <label htmlFor="username">Name:</label>
//           <input
//             name="username"
//             type="text"
//             placeholder="Enter username"
//             onChange={handleChange}
//           />
//           <label htmlFor="password">Name:</label>
//           <input
//             name="password"
//             type="password"
//             placeholder="Enter password"
//             onChange={handleChange}
//           />
//           <input type="submit" className="hover:cursor-pointer" />
//         </form>
//       </>
//     );
//   };

//   return (
//     <>
//       <FormHandler render={form} /> {/* Send the form function as a prop */}
//     </>
//   );
// };

// export default App;

/* Render Props Basic Example: Render Props is a design pattern in React where a component receives a function as a prop and uses that 
function to determine what to render, while sharing its internal state and logic with the rendered output. */
// type ToggleProps = {
//   flag: boolean;
//   render: Function;
// };

// const Toggle = ({ flag, render }: ToggleProps) => {
//   return (
//     <>
//       <h1 className="text-4xl mb-3 font-bold">This is Toggle</h1>
//       {render(flag)}
//     </>
//   );
// };

// const App = () => {
//   return (
//     <div>
//       <Toggle
//         flag={true}
//         render={(isOn: boolean) => {
//           return isOn ? (
//             <div>Toggle Component is On</div>
//           ) : (
//             <div>Toggle Component is Off</div>
//           );
//         }}
//       />
//     </div>
//   );
// };

// export default App;

/* HOC (Higher Order Component) topic Example */
// import AuthDash from "./components/Dashboard";

// const App = () => {
//   return (
//     <>
//       <AuthDash
//         className="bg-slate-700 w-32 h-20 text-white p-4"
//         title="Admin Panel"
//       />
//     </>
//   );
// };

// export default App;

/* Containment & Specialization - Children Example */
// import type { ReactNode } from "react";

// type AlertProps = {
//   children: ReactNode;
//   backgroundColor: string;
// };

// const Alert = ({ children, backgroundColor }: AlertProps) => {
//   return (
//     <div className="flex justify-center items-center min-h-screen ">
//       <div className={`div ${backgroundColor}`}>{children}</div>
//     </div>
//   );
// };

// const DeleteAlert = () => {
//   return (
//     <div>
//       <Alert backgroundColor="bg-gray-700">
//         <h1 className="text-2xl font-bold text-white">Delete Account</h1>
//         <p className="text-white">
//           Are you sure you wanna delete your account?
//         </p>
//         <button className="bg-red-500 p-2 rounded-xl font-bold hover:bg-opacity-85 hover:scale-105 transition-all text-white">
//           Delete Account
//         </button>
//       </Alert>
//     </div>
//   );
// };

// const ConfirmationAlert = () => {
//   return (
//     <div>
//       <Alert backgroundColor="bg-gray-300">
//         <h1 className="text-2xl font-bold">Confirm Account</h1>
//         <p>You need to confirm your email to continue...</p>
//         <button className="bg-green-500 p-2 rounded-xl font-bold hover:bg-opacity-85 hover:scale-105 transition-all">
//           Confirm Account
//         </button>
//       </Alert>
//     </div>
//   );
// };

// const App = () => {
//   return (
//     <div>
//       <ConfirmationAlert />
//       {/* <DeleteAlert /> */}
//     </div>
//   );
// };

// export default App;

/* Custom Hook */
// import { useState, useEffect, useRef } from "react";

// const App = () => {
//   const [day, setDay] = useState("Monday");
//   const prevDay = usePrevious(day);
//   const getNextDay = () => {
//     if (day === "Monday") {
//       setDay("Tuesday");
//     } else if (day === "Tuesday") {
//       setDay("Wednesday");
//     } else if (day === "Wednesday") {
//       setDay("Thursday");
//     } else if (day === "Thursday") {
//       setDay("Friday");
//     } else if (day === "Friday") {
//       setDay("Monday");
//     }
//   };

//   return (
//     <div style={{ padding: "40px" }}>
//       <h1>
//         Today is: {day}
//         <br />
//         {prevDay && <span>Previous work day was: {prevDay}</span>}
//       </h1>
//       <button onClick={getNextDay}>Get next day</button>
//     </div>
//   );
// };

// const usePrevious = (val: string) => {
//   const ref = useRef("");
//   useEffect(() => {
//     ref.current = val;
//   }, [val]);
//   return ref.current;
// };

// export default App;

/* useRef example */
// import { useRef } from "react";

// const App = () => {
//   const inputRef = useRef<HTMLInputElement | null>(null);
//   const focusInput = () => {
//     if (inputRef.current) inputRef.current.focus();
//   };

//   return (
//     <div>
//       <input type="text" ref={inputRef} />
//       <button onClick={focusInput} className="bg-amber-400 m-4 p-2 rounded-xl">
//         Focus Input
//       </button>
//     </div>
//   );
// };

// export default App;

/* useReducer hook */
// import { useReducer } from "react";

// type State = {
//   money: number;
// };

// type Action = {
//   type: string;
// };

// const App = () => {
//   const reducer = (state: State, action: Action) => {
//     switch (action.type) {
//       case "buy_ingredients":
//         return { ...state, money: state.money - 20 };

//       case "sell_a_meal":
//         return { ...state, money: state.money + 30 };

//       case "celebrity_visit":
//         return { ...state, money: state.money + 100 };

//       default:
//         return state;
//     }
//   };

//   const [state, dispatch] = useReducer(reducer, {
//     money: 100,
//   });

//   return (
//     <div className="flex flex-col justify-center items-center">
//       <div className="flex justify-center items-center">
//         <button
//           onClick={() => dispatch({ type: "buy_ingredients" })}
//           className="bg-amber-400 m-4 p-2 rounded-xl"
//         >
//           Buy Ingredients
//         </button>
//         <button
//           onClick={() => dispatch({ type: "sell_a_meal" })}
//           className="bg-amber-400 m-4 p-2 rounded-xl"
//         >
//           Sell A Meal
//         </button>
//         <button
//           onClick={() => dispatch({ type: "celebrity_visit" })}
//           className="bg-amber-400 m-4 p-2 rounded-xl"
//         >
//           Celebrity Visit
//         </button>
//       </div>
//       <h1 className="text-green-500 text-4xl font-bold self-center">
//         {state.money}
//       </h1>
//     </div>
//   );
// };

// export default App;

/* Controlled and validated from */
// import "./App.css";
// import { useState } from "react";
// import { validateEmail } from "./Utils/validateEmail";

// const PasswordErrorMessage = () => {
//   return (
//     <p className="FieldError">Password should have at least 8 characters</p>
//   );
// };

// function App() {
//   const [firstName, setFirstName] = useState("");
//   const [lastName, setLastName] = useState("");
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState({
//     value: "",
//     isTouched: false,
//   });
//   const [role, setRole] = useState("role");

// const getIsFormValid = () => {
//   // My solution
//   if (
//     firstName === "" ||
//     email === "" ||
//     password.value === "" ||
//     role === "role"
//   )
//     return false;
//   if (password.value.length < 8) return false;
//   if (!validateEmail(email)) return false;
//   return true;

//   // Better and readable solution
//   // const getIsFormValid = () => {
//   //   return (
//   //     firstName &&
//   //     validateEmail(email) &&
//   //     password.value.length >= 8 &&
//   //     role !== "role"
//   //   );
//   // };
// };

//   const clearForm = () => {
//     setFirstName("");
//     setLastName("");
//     setEmail("");
//     setPassword({ value: "", isTouched: false });
//     setRole("role");
//   };

//   const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
//     e.preventDefault();
//     alert("Account created!");
//     clearForm();
//   };

//   return (
//     <div className="App">
//       <form onSubmit={handleSubmit}>
//         <fieldset>
//           <h2>Sign Up</h2>
//           <div className="Field">
//             <label>
//               First name <sup>*</sup>
//             </label>
//             <input
//               placeholder="First name"
//               type="text"
//               onChange={(e) => setFirstName(e.target.value)}
//               value={firstName}
//             />
//           </div>
//           <div className="Field">
//             <label>Last name</label>
//             <input
//               placeholder="Last name"
//               type="text"
//               onChange={(e) => setLastName(e.target.value)}
//               value={lastName}
//             />
//           </div>
//           <div className="Field">
//             <label>
//               Email address <sup>*</sup>
//             </label>
//             <input
//               placeholder="Email address"
//               type="email"
//               onChange={(e) => setEmail(e.target.value)}
//               value={email}
//             />
//           </div>
//           <div className="Field">
//             <label>
//               Password <sup>*</sup>
//             </label>
//             <input
//              placeholder="Password"
//              type="password"
//              onChange={(e) => setPassword({ value: e.target.value, isTouched: true })} // My solution
//              // Another Solution
//              // onChange={(e) => {
//              //   setPassword({ ...password, value: e.target.value });
//              // }}
//              // onBlur={() => {
//              //   setPassword({ ...password, isTouched: true });
//              // }}
//              value={password.value}
//             >;
//             {password.isTouched && password.value.length < 8 ? (
//               <PasswordErrorMessage />
//             ) : (
//               false
//             )}
//           </div>
//           <div className="Field mt-6">
//             <label>
//               Role <sup>*</sup>
//             </label>
//             <select onChange={(e) => setRole(e.target.value)} value={role}>
//               <option value="role">Role</option>
//               <option value="individual">Individual</option>
//               <option value="business">Business</option>
//             </select>
//           </div>
//           <button type="submit" disabled={!getIsFormValid()}>
//             Create account
//           </button>
//         </fieldset>
//       </form>
//     </div>
//   );
// }

// export default App;

/* React "Keys" for list elements */
// import "./App.css";
// import DessertsList from "./components/DessertsList";

// const desserts = [
//   {
//     id: 1,
//     name: "Chocolate Cake",
//     calories: 400,
//     createdAt: "2022-09-01",
//   },
//   {
//     id: 2,
//     name: "Ice Cream",
//     calories: 200,
//     createdAt: "2022-01-02",
//   },
//   {
//     id: 3,
//     name: "Tiramisu",
//     calories: 300,
//     createdAt: "2021-10-03",
//   },
//   {
//     id: 4,
//     name: "Cheesecake",
//     calories: 600,
//     createdAt: "2022-01-04",
//   },
// ];

// function App() {
//   return (
//     <div className="App">
//       <h2>List of low calorie desserts:</h2>
//       <DessertsList data={desserts} />
//     </div>
//   );
// }

// export default App;

// const App = () => {
//   return (
//     <div>
//     </div>
//   );
// }

// export default App;
