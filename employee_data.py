import random

names = ["Ali", "Sara", "Usman", "Ayesha", "Bilal", "Zara"]
skills_list = ["Python", "Java", "HTML", "CSS", "JavaScript", "SQL"]
companies = ["C001", "C002", "C003"]

employees = []

for i in range(1, 101):
    emp = {
        "employee_id": f"E{i:03}",
        "name": random.choice(names),
        "company_id": random.choice(companies),
        "skills": random.sample(skills_list, 3)
    }
    employees.append(emp)

for e in employees:
    print(e)
