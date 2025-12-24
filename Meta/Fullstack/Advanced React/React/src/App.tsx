const App = () => {
  return <div></div>;
};

export default App;

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
