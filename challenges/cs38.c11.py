names_and_genders = [
    ["Sarah", "F"],
    ["Rickie", "M"],
    ["Rob", "M"],
    ["Charlie", "M"],
    ["Daisy", "F"],
]

for name, gender in names_and_genders:
    if gender == "M":
        print(name, "is male")
    else:
        print(name, "is female")
