values = [
    [4, 7, 9, 12],
    [0, 1, 8, 13],
    [1, 2, 12, 14],
    [7, 8, 9, 11],
]

for column in range(len(values[0])):
    column_total = 0

    for row in range(len(values)):
        column_total += values[row][column]

    column_mean = column_total / len(values)
    print("Column", column + 1, "mean:", column_mean)
