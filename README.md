## Game Boy ROM Toolkit

<img src="https://user-images.githubusercontent.com/17799879/220471133-00be7357-4d28-4f91-8e82-932bb2a06783.gif" alt="GameboyBoyGIF" width="150" height="150">


This Python script provides a command-line interface for working with Game Boy ROM files. The script offers two main features:

1. **Checking a checksum**: Given a checksum, the script checks if it exists in a JSON file that maps checksums to filenames. If a match is found, the script returns the filename.
2. **Scanning a directory for ROM files**: The script scans a specified directory for Game Boy ROM files (files with a ".gb" extension), calculates the CRC-32 checksum for each file, and writes the checksums and corresponding filenames to a JSON file.

The script uses standard Python libraries like `os`, `json`, and `zlib`, as well as a third-party library called `prompt_toolkit` for handling user input. 

The script presents a simple menu with three options: Check a checksum, Scan the roms folder, or Exit. The user can input their choice, and the corresponding function will be called. 

Overall, this Python script is a simple but useful tool for working with Game Boy ROM files from the command line.

🤞The goal is to extend this toolkit to include other things I may need.
