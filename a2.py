import csv

# Below is a "good" solution.
highest_salary = 0
highest_salary_employee = None
salary_list = []
f = open("employees.csv", "r")
try:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        salary = float(row["salary"])
        if row["employee_type"] == "Manager":
            salary_list.append(salary)
        if salary > highest_salary:
            highest_salary = salary
            highest_salary_employee = row
finally:
    f.close()
average = sum(salary_list) / len(salary_list)
name = f"{highest_salary_employee['first_name']} {highest_salary_employee['last_name']}"
print(f"The average salary of managers is {average:,.0f} dollars.")
print(f"{name} has the highest salary (${highest_salary:.2f}).")


# Below is a "very good" solution. It may require some Googling.
# import operator
# f = open("employees.csv", "r")
# try:
#     csv_reader = csv.DictReader(f)
#     employees = [{"name": f"{row['first_name']} {row['last_name']}",
#                   "type": row["employee_type"],
#                   "salary": float(row["salary"])} for row in csv_reader]
#     managers = [emp for emp in employees if emp["type"] == "Manager"]
#     average = sum(m["salary"] for m in managers) / len(managers)
#     highest_salary_employee = max(employees, key=operator.itemgetter("salary"))
# finally:
#     f.close()
#
# print(f"The average salary of managers is {average:,.0f} dollars.")
# print(f"{highest_salary_employee['name']} has the highest salary (${highest_salary_employee['salary']:.2f}).")
