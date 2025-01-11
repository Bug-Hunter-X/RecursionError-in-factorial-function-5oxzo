# RecursionError in Factorial Function
This repository contains a Python code example demonstrating a common error in recursive functions: the `RecursionError`. The `factorial` function is implemented recursively, but it lacks a proper base case for negative input, leading to infinite recursion. The solution demonstrates how to handle negative input appropriately and prevent the error.
## Bug
The original `factorial` function recursively calculates the factorial of a number.  However, when a negative number is passed, the recursion never stops, resulting in a `RecursionError`. 
## Solution
The solution adds a check at the beginning to handle the case of negative input, returning an error message or raising a ValueError, preventing the infinite recursion.