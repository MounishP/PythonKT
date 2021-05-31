baseSalary = int(input("Enter the current salary: "))
currentYear = 2021
currentMonth = 6
resignYear = 2023
resignMonth = 4
hikePercentage = 30 / 100
period = 6
count = 0


def hike(baseSalary, hikePercentage):  # 30000,0.3, 39000-0.3
    return (baseSalary * hikePercentage) + baseSalary  # 39000


while currentYear != resignYear:  # 2022 != 2023
    count += 1  # 1,2,3,4,5,6
    if count == 6:  #
        baseSalary = hike(baseSalary, hikePercentage)  # 39000, 50700, x, y
        currentMonth = currentMonth + 6  # 12, 18
        count = 0  # 0

        if currentMonth > 12:  # 18 > 12
            currentMonth = currentMonth - 12  # 6
            currentYear += 1  # 2022, 2023

print(f'The salary at the time of resigning is {baseSalary}')
