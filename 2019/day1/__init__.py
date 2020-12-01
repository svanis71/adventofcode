from indata.day1_input import input_data


def calcFuel(x):
    return 0 if x < 2 else x // 3 - 2


print('Day 1')
# Part 1
print(sum([calcFuel(x) for x in input_data]))

# Part 2
fuelRequirements = []
for x in input_data:
    fuel = calcFuel(x)
    while fuel > 0:
        fuelRequirements.append(fuel)
        fuel = calcFuel(fuel)
print(sum(fuelRequirements))
