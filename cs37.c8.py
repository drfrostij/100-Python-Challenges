def text_file_size_in_kb(bits_per_character, number_of_characters):
    size_in_bits = bits_per_character * number_of_characters
    return size_in_bits / 8 / 1024


bits_per_character = int(input("Enter the bits per character: "))
number_of_characters = int(input("Enter the number of characters: "))
print(
    "Text file size:",
    text_file_size_in_kb(bits_per_character, number_of_characters),
    "KB",
)
