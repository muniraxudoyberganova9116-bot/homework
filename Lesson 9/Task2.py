# #### Task 2: Student Grades Management
# 1. Create a CSV file named `grades.csv` with the following structure:
#    csv
#    Name,Subject,Grade
#    Alice,Math,85
#    Bob,Science,78
#    Carol,Math,92
#    Dave,History,74
   
# 2. Write a Python program to:
#    - Read data from `grades.csv` and store it in an appropriate data structure (e.g., a list of dictionaries).
#    - Calculate the average grade for each subject.
#    - Write a new CSV file named `average_grades.csv` with the following structure:
#      csv
#      Subject,Average Grade
#      Math,88.5
#      Science,78
#      History,74
     
# 3. Use the `csv` module for reading and writing the CSV files.

# ---

import csv
from collections import defaultdict

INPUT_FILE  = "grades.csv"
OUTPUT_FILE = "average_grades.csv"

with open(INPUT_FILE, newline="") as f:
    records = list(csv.DictReader(f))          # [{'Name':..., 'Subject':..., 'Grade':...}, ...]

subject_grades: dict[str, list[float]] = defaultdict(list)

for row in records:
    subject_grades[row["Subject"]].append(float(row["Grade"]))

averages = {
    subject: sum(grades) / len(grades)
    for subject, grades in subject_grades.items()
}

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Subject", "Average Grade"])
    writer.writeheader()
    writer.writerows(
        {"Subject": subject, "Average Grade": avg}
        for subject, avg in averages.items()
    )

print(f"{'Subject':<12} {'Average Grade':>13}")
print("-" * 26)
for subject, avg in averages.items():
    print(f"{subject:<12} {avg:>13.1f}")

print(f"\n✔  Results saved to '{OUTPUT_FILE}'")