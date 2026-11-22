total = 0

for i in range(1, 4):
    for j in range(1, 4):
        num = i * j
        total += num
        print("i:", i, "j:", j, "num:", num, "total:", total)

print(total)
