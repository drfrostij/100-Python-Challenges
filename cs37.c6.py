def sound_file_size(sample_rate, duration, bit_depth):
    return sample_rate * duration * bit_depth


sample_rate = int(input("Enter the sample rate: "))
duration = int(input("Enter the duration in seconds: "))
bit_depth = int(input("Enter the bit depth: "))
print("Sound file size:", sound_file_size(sample_rate, duration, bit_depth), "bits")
