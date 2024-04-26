grades = [35, 67, 98, 100, 100]
total = 0
#total = sum(grades) with no for
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)