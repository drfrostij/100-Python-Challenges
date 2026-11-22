def text_file_size(bits_per_character, number_of_characters):
    return bits_per_character * number_of_characters


bits_per_character = int(input("Enter the bits per character: "))
number_of_characters = int(input("Enter the number of characters: "))
print("Text file size:", text_file_size(bits_per_character, number_of_characters), "bits")
