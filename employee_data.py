import random
import json

# Sample data
names = ["Ali", "Sara", "Usman", "Ayesha", "Bilal", "Zara"]
skills_list = ["Python", "Java", "HTML", "CSS", "JavaScript", "SQL"]
companies = ["C001", "C002", "C003"]

# 🔢 Generate 100 employees
employees = []
for i in range(1, 101):
    emp = {
        "employee_id": f"E{i:03}",
        "name": random.choice(names),
        "company_id": random.choice(companies),
        "skills": random.sample(skills_list, 3)
    }
    employees.append(emp)

# ➕ Add a new employee
employees.append({
    "employee_id": "E101",
    "name": "Hamza",
    "company_id": "C002",
    "skills": ["Python", "SQL", "CSS"]
})

# Update employee E050
for emp in employees:
    if emp["employee_id"] == "E050":
        emp["name"] = "Fatima"
        emp["skills"] = ["Java", "CSS"]
        break

# Remove employee E025
employees = [emp for emp in employees if emp["employee_id"] != "E025"]

# Print all employees
print(json.dumps(employees, indent=4))
