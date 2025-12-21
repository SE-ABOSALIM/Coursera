const addFive = require("./addFive").addFive;
const divide = require("./addFive").divide;

test("returns the number plus 5", () => {
  expect(addFive(1)).toBe(6);
});

test("returns the result of num1 divided by num2", () => {
  expect(divide(5, 2)).toBe(2.5);
});

test("returns the result of num1 divided by num2", () => {
  expect(divide(5, 0)).toBe("Cannot divide by 0");
});
