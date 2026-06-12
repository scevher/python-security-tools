log_file = input("Enter log file path: ")
keyword = input("Enter keyword to search: ")

try:
    with open(log_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    print("\nMatching Log Lines:")

    for line_number, line in enumerate(lines, start=1):
        if keyword.lower() in line.lower():
            print(f"Line {line_number}: {line.strip()}")

except FileNotFoundError:
    print("Error: Log file not found.")
