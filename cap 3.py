def process_line(line):
    left_pointer = 0
    right_pointer = len(line) - 1

    left_number = None
    right_number = None

    while left_pointer < len(line) and right_pointer >= 0:
        if left_number is None and line[left_pointer].isdigit():
            left_number = line[left_pointer]
        else:
            left_pointer += 1

        if right_number is None and line[right_pointer].isdigit():
            right_number = line[right_pointer]
        else:
            right_pointer -= 1

        if left_number is not None and right_number is not None:
            break

    if left_number is not None and right_number is not None:
        return int(left_number + right_number)
    elif left_number is not None:
        return int(left_number * 2)
    elif right_number is not None:
        return int(right_number * 2)
    else:
        return 0

def main():
    file_path = "C:\\Users\\User\\Documents\\CSF\\405.txt"

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        total_sum = 0

        for line in lines:
            line = line.strip()  # Remove any leading/trailing whitespace
            two_digit_number = process_line(line)
            total_sum += two_digit_number

        print("The sum of all two-digit numbers is:", total_sum)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Run the main function
if __name__ == "__main__":
    main()
