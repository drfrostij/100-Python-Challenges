import time


def sub_flash():
    print("Turn Lights on")
    time.sleep(1)
    print("Turn Lamp off")
    time.sleep(1)


sun_off = input("Is the sun off? (yes/no): ").lower()

if sun_off == "yes":
    print("Turn Lights on")
    sub_flash()
else:
    print("Turn Lights off")
