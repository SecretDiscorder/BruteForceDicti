import itertools
import string
alphabet = input("Enter the alphabet range (a-z, 0-9): ")  # Get input for alphabet range
length = int(input("Enter the length of permutations: "))  # Get input for permutation length

# Validate the alphabet input
valid_chars = string.ascii_lowercase + string.digits
if any(char not in valid_chars for char in alphabet):
    print("Invalid alphabet range. Please enter a valid range (a-z, 0-9).")
else:
    # Generate permutations
    permutations = itertools.product(alphabet, repeat=length)

    # Create and open the output file in write mode
    output_file = "output.txt"
    with open(output_file, "w") as f:
        for combination in permutations:
            # Join the characters and write to the file
            f.write("".join(combination) + "\n")

    print(f"Permutations of length {length} saved to {output_file}")
