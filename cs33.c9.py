stream = "stream"
number = 5678
light = "light"
magic = "magic"


password = (stream[0] + str(number)[:2] + light[2] + light[0] + light[3] + magic[3:].upper())

print("Password:", password)