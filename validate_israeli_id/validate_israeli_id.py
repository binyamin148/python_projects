def validate_israeli_id(id_number):
    if not id_number.isdigit() or len(id_number) != 9:
        return False
    
    first_8_digits = id_number[:8]
    
    total_sum = 0
    for index, digit in enumerate(first_8_digits, start=1):
        digit = int(digit)
        if index % 2 == 0:
            doubled = digit * 2
            total_sum += doubled if doubled < 10 else doubled // 10 + doubled % 10
        else:
            total_sum += digit
    
    next_multiple_of_10 = (total_sum // 10 + 1) * 10
    calculated_check_digit = next_multiple_of_10 - total_sum
    
    return calculated_check_digit == int(id_number[-1])

def main():
    print("Israeli ID Number Validator")
    print("---------------------------")
    
    while True:
        id_number = input("Enter an Israeli ID number (9 digits) or 'q' to quit: ")
        
        if id_number.lower() == 'q':
            print("Thank you for using the Israeli ID Number Validator. Goodbye!")
            break
        
        if validate_israeli_id(id_number):
            print("Valid ID Number")
        else:
            print("Invalid ID Number")
        
        print()  

if __name__ == "__main__":
    main()
            