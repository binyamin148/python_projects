# Nested String Checker

## Purpose
This project implements a Python function to check if a given string is "properly nested". A string is considered properly nested if it meets one of the following conditions:
1. It is empty
2. It has the form "(U)", "[U]", or "{U}" where U is a properly nested string
3. It has the form "VW" where V and W are properly nested strings

## Code Description

### Main Function: `is_properly_nested`
This function takes a string `S` as input and returns `True` if the string is properly nested, and `False` otherwise.

#### Algorithm:
- Uses a stack to keep track of opening brackets.
- Iterates through each character in the input string.
- If an opening bracket is encountered, it's pushed onto the stack.
- If a closing bracket is encountered, it checks if it matches the last opening bracket on the stack.
- Returns `True` if all brackets are properly closed and matched, `False` otherwise.

### Test Function: `test`
This function tests the `is_properly_nested` function with a set of predefined test cases.

## Usage
To use this code:
1. Copy the `is_properly_nested` function into your Python project.
2. Call the function with a string argument:
   ```python
   result = is_properly_nested("([{}])")
   print(result)  # Should print True
   ```

3. To run the tests, call the `test` function with `is_properly_nested` as an argument:
   ```python
   test(is_properly_nested)
   ```

## Constraints
- The input string `S` consists of N characters: '(', '{', '[', ']', '}', or ')'.
- N is an integer within the range [0..200,000].

## Time and Space Complexity
- Time Complexity: O(N), where N is the length of the input string.
- Space Complexity: O(N) in the worst case, where all characters are opening brackets.

## Note
There is a potential issue in the test function with one of the "legal" test cases: '[[]([]]]{}'. This string is not actually properly nested and should be removed or corrected in the test cases.