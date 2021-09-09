import csv

# Below is a "good" solution.
# lowest_salary = 99999999
# lowest_salary_employee = None
# salary_list = []
# f = open("employees.csv", "r")
# try:
#     csv_reader = csv.DictReader(f)
#     for row in csv_reader:
#         salary = float(row["salary"])
#         if row["employee_type"] == "Manager":
#             salary_list.append(salary)
#         if salary < lowest_salary:
#             lowest_salary = salary
#             lowest_salary_employee = row
# finally:
#     f.close()
# average = sum(salary_list) / len(salary_list)
# name = f"{lowest_salary_employee['first_name']} {lowest_salary_employee['last_name']}"
# print(f"The average salary of managers is {average:,.0f} dollars.")
# print(f"{name} has the lowest salary (${lowest_salary:.2f}).")


# Below is a "very good" solution. It may require some Googling.
f = open("employees.csv", "r")
try:
    csv_reader = csv.DictReader(f)
    employees = [{"name": f"{row['first_name']} {row['last_name']}",
                  "type": row["employee_type"],
                  "salary": float(row["salary"])} for row in csv_reader]
    managers = [emp for emp in employees if emp["type"] == "Manager"]
    average = sum(m["salary"] for m in managers) / len(managers)
    lowest_salary_employee = min(employees, key=lambda emp: emp["salary"])
finally:
    f.close()

print(f"The average salary of managers is {average:,.0f} dollars.")
print(f"{lowest_salary_employee['name']} has the highest salary (${lowest_salary_employee['salary']:.2f}).")
