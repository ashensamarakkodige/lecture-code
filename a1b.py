number_group_1 = input("Enter number group 1: ")
number_group_2 = input("Enter number group 2: ")

set1 = set([int(part) for part in number_group_1.split()])
set2 = set([int(part) for part in number_group_2.split()])

results = [str(i) for i in set1 & set2]
print("Result:", " ".join(results))
