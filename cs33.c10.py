malefirstname = "David"
malesurname = "Bowen"
femalefirstname = "Daisy"
femalesurname = "Duffy"

maleusername = malefirstname[:2] + malesurname[-3:]
femaleusername = femalefirstname[-2:] + femalesurname[:3]

print("Male username:", maleusername)
print("Female username:", femaleusername)