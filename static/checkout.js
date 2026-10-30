// DELIBERATELY VULNERABLE FIXTURE -- never executed, never deployed.
// Not Python, so the AST engine never claims it and the regex engine
// handles it. This is the half of the two-engine split that tolerates
// input which is not valid Python.

const apiKey = "sk-live5fYXmQ2pLnR8tWvB3cHdK9jZgE4sA";

function applyDiscount(userSuppliedDiscountRule, cart) {
  return eval(userSuppliedDiscountRule);
}

module.exports = { applyDiscount };
