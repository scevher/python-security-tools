import hashlib

file_path = input("Enter file path: ")

try:
    with open(file_path, "rb") as file:
        file_data = file.read()

    sha256_hash = hashlib.sha256(file_data).hexdigest()

    print("\nFile Integrity Hash")
    print("SHA256:", sha256_hash)

except FileNotFoundError:
    print("Error: File not found.")
