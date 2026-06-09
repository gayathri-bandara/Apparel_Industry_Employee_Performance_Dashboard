import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

# ---------------------------
# 1. Generate Employees Table
# ---------------------------

num_employees = 50

departments = ['Cutting', 'Sewing', 'Finishing', 'Quality Control']

employees = []

for i in range(num_employees):
    employees.append([
        i + 1,
        fake.name(),
        np.random.choice(departments),
        np.random.randint(20000, 60000)  # Salary
    ])

employees_df = pd.DataFrame(employees, columns=[
    "EmployeeID", "EmployeeName", "Department", "Salary"
])

# ---------------------------
# 2. Generate Performance Table
# ---------------------------

dates = pd.date_range(start="2024-01-01", end="2024-03-31")

performance_data = []

for emp_id in employees_df['EmployeeID']:
    for date in dates:
        performance_data.append([
            emp_id,
            date,
            np.random.randint(50, 150),   # Units produced
            np.random.randint(0, 10),     # Defects
            np.random.choice([0, 1], p=[0.1, 0.9]),  # Attendance
            np.random.randint(0, 4)       # Overtime hours
        ])

performance_df = pd.DataFrame(performance_data, columns=[
    "EmployeeID", "Date", "UnitsProduced", "Defects", "Attendance", "OvertimeHours"
])

# ---------------------------
# 3. Save Files
# ---------------------------

employees_df.to_csv("employees.csv", index=False)
performance_df.to_csv("performance.csv", index=False)

print("✅ Data generated successfully!")