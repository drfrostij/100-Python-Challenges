file = open("tracks.txt", "r")

for line in file:
    artist, song, duration = line.strip().split(",")
    print("Artist:", artist)
    print("Song:", song)
    print("Duration:", duration)

file.close()
