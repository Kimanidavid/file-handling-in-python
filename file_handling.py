# Read the file
filename = input("Enter the filename to read: ")

try:
    with open(filename, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        print("File read successfully.")
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
    exit(1)

# Modify content
modified_content = content.upper()

# Write to a new file
output_filename = "modified_" + filename
try:
    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.write(modified_content)
        print(f"Modified content written to '{output_filename}'.")

        # See results of new file
        with open(output_filename, "r", encoding="utf-8") as infile:
            print("Contents of the modified file:")
            print(infile.read())

except Exception as e:
    print(f"Error writing to file: {e}")
    exit(1)