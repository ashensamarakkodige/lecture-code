lower = int(input("Lower bound: "))
upper = int(input("Upper bound: "))
answer = 0
for number_of_this_round in range(lower, upper + 1):
    answer = answer + number_of_this_round
print("Total = ", answer)
