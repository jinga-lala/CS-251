#! python3

employees = open('employees.txt', 'r')

for line in employees:
    name = line.split(" ")[0]
    correctName = name[3:] + name[0:3]
    print(correctName)
