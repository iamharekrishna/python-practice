line = "This is a sample line with a number 123.45 at the end."

# Find the position of the last occurrence of a digit in the line
end_of_number_pos = line.rfind(" ") + 1

# Extract the number at the end of the line using string slicing
number_str = line[end_of_number_pos:]

# Convert the extracted value to a floating-point number
extracted_number = float(number_str)

# Print the extracted floating-point number
print(extracted_number)
