def extract_calibration(line):
    # Initialize variables
    first_digit = None
    last_digit = None

    # Iterate through the characters in the line
    for char in line:
        # Check if the character is a digit
        # If first_digit is None, assign the current digit to it
        # Else assign the current digit to last_digit
        if char.isdigit():

            if first_digit is None:
                first_digit = char
            last_digit = char

    # Check first_digit and last_digit
    if first_digit is not None and last_digit is not None:
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
