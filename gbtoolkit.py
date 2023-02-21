import os
import json
import zlib
from prompt_toolkit import prompt

def calculate_checksum(file_path):
    """Calculate the CRC-32 checksum for a given file"""
    with open(file_path, 'rb') as f:
        return hex(zlib.crc32(f.read()) & 0xffffffff)

def check_checksum(checksum, checksum_file):
    """Check the given checksum against the checksums in the specified file"""
    if not os.path.exists(checksum_file):
        print(f"{checksum_file} does not exist.")
        return None
    # Open the checksum file
    with open(checksum_file, 'r') as f:
        data = json.load(f)
        if checksum in data:
            return data[checksum]
    # Return None if no match is found
    return None

def write_json(folder_path, json_file):
    data = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.gb'):
            file_path = os.path.join(folder_path, filename)
            checksum = calculate_checksum(file_path)
            data[checksum] = filename
    with open(json_file, 'w') as f:
        json.dump(data, f)

def clear(): 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def main():
    print("GB Rom Toolkit\n")
    print("--------------------------------------------------")
    print("Please select an option from the following:")
    print("1. Check a checksum")
    print("2. Scan the roms folder")
    print("3. Exit")
    print("--------------------------------------------------")

    folder_path = '/home/dev/code/gbchecksum/roms'
    checksum_file = '/home/dev/code/gbchecksum/roms.json'

    while True:
        choice = prompt("Enter your choice: ")
        if choice == "1":
            checksum = prompt("Enter the checksum to check: ")
            name = check_checksum(checksum, checksum_file)
            if name:
                print(f'The checksum belongs to the file: {name}')
            else:
                print("No match found for the given checksum.")
        elif choice == "2":
            if not os.path.exists(folder_path):
                print(f"{folder_path} does not exist.")
            elif not os.listdir(folder_path):
                print(f"There are no files in {folder_path}.")
            else:
                write_json(folder_path, checksum_file)
                print("File created successfully")
        elif choice == "3":
            break
        else:
            print("Invalid choice, please enter a valid number.")

if __name__ == '__main__':
    main()

