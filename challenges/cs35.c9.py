remaining_score = 100

for dart in range(1, 4):
    score = int(input("Input score from dart:", dart))
    remaining_score -= score
    print(remaining_score)

    if remaining_score == 0:
        print("Game shot!")
        break
    if remaining_score < 0:
        remaining_score = 100
        print("Bust!")
        break
    if dart < 3:
        print("Throw the next dart")
else:
    print("You failed to win.")
