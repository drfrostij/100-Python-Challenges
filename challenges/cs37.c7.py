def image_file_size(colour_depth, height, width):
    return colour_depth * height * width


colour_depth = int(input("Enter the colour depth: "))
height = int(input("Enter the image height in pixels: "))
width = int(input("Enter the image width in pixels: "))
print("Image file size:", image_file_size(colour_depth, height, width), "bits")
