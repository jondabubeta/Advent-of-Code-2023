import re

word_to_digit = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def extract_calibration(line):
    # Initialize variables
    first_digit = None
    last_digit = None

    # Iterate through the characters in the line
    for char in line:
        # Construct the number by grabbing the first iteration of a digit or key
        number = ""
        first_digit = None
        last_digit = None

        for ch in line:
            digit = None
            if ch.isdigit():
                digit = ch
            else:
                number += ch
                for k, v in word_to_digit.items():
                    if number.endswith(k):
                        digit = str(v)
            if digit is not None:
                last_digit = digit
                if first_digit is None:
                    first_digit = digit

    # Check first_digit and last_digit
    if first_digit is not None and last_digit is not None:
        print(int(first_digit + last_digit))
        return int(first_digit + last_digit)
    else:
        return 0


def calculate_calibration(file_path):
    # Initialize a variable to store the sum
    total_sum = 0

    # Open the file for reading
    with open(file_path, 'r') as file:
        # Read each line from the file
        for line in file:
            # Strip any leading/trailing whitespace and newline characters
            line = line.strip()

            # Check if the line is not empty
            if line:
                # Extract the calibration value for this line
                calibration_value = extract_calibration(line)

                # Add the calibration value for this line to the total sum
                total_sum += calibration_value

    return total_sum


print("Calibration Sum:", calculate_calibration('input.txt'))
