import itertools
import string
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"# Get input for alphabet range
length =  8 # Get input for permutation length

# Validate the alphabet input
valid_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
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
 output file in write mode
    output_file = "output.txt"
    with open(output_file, "w") as f:
        for combination in permutations:
            # Join the characters and write to the file
            f.write("".join(combination) + "\n")

    print(f"Permutations of length {length} saved to {output_file}")
    output_file2 = "output2.txt"
    with open(output_file2, "w") as f:
        for combination2 in permutations2:
            # Join the characters and write to the file
            f.write("".join(combination2) + "\n")

    print(f"Permutations of length {length} saved to {output_file2}")
    output_file3 = "output3.txt"
    with open(output_file3, "w") as f:
        for combination3 in permutations3:
            # Join the characters and write to the file
            f.write("".join(combination3) + "\n")

    print(f"Permutations of length {length} saved to {output_file3}")
    output_file4 = "output4.txt"
    with open(output_file4, "w") as f:
        for combination4 in permutations4:
            # Join the characters and write to the file
            f.write("".join(combination4) + "\n")

    print(f"Permutations of length {length} saved to {output_file4}")
    output_file5 = "output5.txt"
    with open(output_file5, "w") as f:
        for combination5 in permutations5:
            # Join the characters and write to the file
            f.write("".join(combination5) + "\n")

    print(f"Permutations of length {length} saved to {output_file5}")
    output_file6 = "output6.txt"
    with open(output_file6, "w") as f:
        for combination6 in permutations6:
            # Join the characters and write to the file
            f.write("".join(combination6) + "\n")

    print(f"Permutations of length {length} saved to {output_file6}")
    



    


