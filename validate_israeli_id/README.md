# python_projects

# Israeli ID Number Validator

## Description
This Python script implements an algorithm to validate Israeli ID numbers. It allows users to input ID numbers and provides immediate feedback on their validity.

## System Requirements
- Python 3.x

## Installation
1. Download the `israeli_id_validator.py` file to your computer.
2. Ensure you have Python 3.x installed on your system.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing the `israeli_id_validator.py` file.
3. Run the script using the command:
   ```
   python israeli_id_validator.py
   ```
4. Enter a 9-digit Israeli ID number when prompted.
5. The script will display whether the ID number is valid or not.
6. Type 'q' to exit the program.

## How It Works
The algorithm operates as follows:
1. Checks if the input is exactly 9 digits.
2. Isolates the first 8 digits.
3. Performs a special calculation on each digit based on its position:
   - Odd positions: multiplies by 1
   - Even positions: multiplies by 2 (if the result is two digits, sums those digits)
4. Sums all the results.
5. Calculates the check digit by finding the difference between the sum and the next multiple of 10.
6. Compares the calculated check digit with the 9th digit of the input.

## Examples
- Valid ID number: 123456782
- Invalid ID number: 123456789

## Contributing
Feel free to suggest improvements or report bugs by opening an issue or submitting a pull request.

## License
This project is distributed under the MIT License. See the `LICENSE` file for more information.