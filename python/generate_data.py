import csv
import random
from pathlib import Path

# ---------------------------------------------------------
# SMART CAMPUS ANALYTICS
# Fictional college data generator
# College: Sunrise Institute of Technology
# ---------------------------------------------------------

# Find the main project folder
PROJECT_FOLDER = Path(__file__).resolve().parent.parent

# Data folder
DATA_FOLDER = PROJECT_FOLDER / "data"

# Create data folder if it doesn't exist
DATA_FOLDER.mkdir(exist_ok=True)

# Make results repeatable
random.seed(42)

# ---------------------------------------------------------
# BASIC COLLEGE INFORMATION
# ---------------------------------------------------------

departments = [
    (1, "CSE"),
    (2, "AIML"),
    (3, "ECE"),
    (4, "EEE"),
    (5, "MECH")
]

skills = [
    (1, "Python"),
    (2, "SQL"),
    (3, "Excel"),
    (4, "Power BI"),
    (5, "Java"),
    (6, "JavaScript"),
    (7, "HTML"),
    (8, "CSS"),
    (9, "Machine Learning"),
    (10, "Deep Learning"),
    (11, "Tableau"),
    (12, "AWS"),
    (13, "Git"),
    (14, "Data Structures"),
    (15, "Communication")
]

companies = [
    (1, "TechVista", "IT Services", "Hyderabad"),
    (2, "DataBridge", "Analytics", "Bangalore"),
    (3, "CloudNest", "Cloud Technology", "Hyderabad"),
    (4, "CodeSphere", "Software", "Bangalore"),
    (5, "InsightLabs", "Data Analytics", "Hyderabad"),
    (6, "NextWave Technologies", "IT Services", "Bangalore"),
    (7, "ByteWorks", "Software", "Hyderabad"),
    (8, "InnovateHub", "Technology", "Bangalore")
]

# ---------------------------------------------------------
# HELPER FUNCTION
# ---------------------------------------------------------

def save_csv(filename, headers, rows):
    file_path = DATA_FOLDER / filename

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"Created: {filename}")


# ---------------------------------------------------------
# 1. CREATE STUDENTS
# ---------------------------------------------------------

students = []

for i in range(1, 1001):

    student_id = 1000 + i
    student_name = f"Student_{i:04d}"

    department_id, department_name = random.choice(departments)

    year = random.choice([1, 2, 3, 4])

    # CGPA between 5.50 and 9.80
    cgpa = round(random.uniform(5.50, 9.80), 2)

    students.append([
        student_id,
        student_name,
        department_id,
        department_name,
        year,
        cgpa
    ])

save_csv(
    "students.csv",
    [
        "student_id",
        "student_name",
        "department_id",
        "department_name",
        "year",
        "cgpa"
    ],
    students
)


# ---------------------------------------------------------
# 2. CREATE ATTENDANCE
# ---------------------------------------------------------

attendance = []

for student in students:

    student_id = student[0]

    attendance_percentage = round(
        random.uniform(55, 98), 2
    )

    attendance.append([
        student_id,
        attendance_percentage
    ])

save_csv(
    "attendance.csv",
    [
        "student_id",
        "attendance_percentage"
    ],
    attendance
)


# ---------------------------------------------------------
# 3. CREATE ACADEMIC PERFORMANCE
# ---------------------------------------------------------

subjects = [
    "Python Programming",
    "DBMS",
    "Mathematics",
    "Machine Learning",
    "Computer Networks"
]

academic_performance = []

for student in students:

    student_id = student[0]
    cgpa = student[5]

    for subject in subjects:

        # Convert CGPA roughly into marks
        base_marks = cgpa * 10

        marks = int(
            max(
                40,
                min(
                    100,
                    random.gauss(base_marks, 8)
                )
            )
        )

        academic_performance.append([
            student_id,
            subject,
            marks
        ])

save_csv(
    "academic_performance.csv",
    [
        "student_id",
        "subject",
        "marks"
    ],
    academic_performance
)


# ---------------------------------------------------------
# 4. CREATE STUDENT SKILLS
# ---------------------------------------------------------

student_skills = []

for student in students:

    student_id = student[0]

    # Better academic performance = slightly more skills
    cgpa = student[5]

    if cgpa >= 8.5:
        number_of_skills = random.randint(4, 7)
    elif cgpa >= 7.0:
        number_of_skills = random.randint(3, 5)
    else:
        number_of_skills = random.randint(2, 4)

    selected_skills = random.sample(
        skills,
        number_of_skills
    )

    for skill_id, skill_name in selected_skills:

        student_skills.append([
            student_id,
            skill_id,
            skill_name
        ])

save_csv(
    "student_skills.csv",
    [
        "student_id",
        "skill_id",
        "skill_name"
    ],
    student_skills
)


# ---------------------------------------------------------
# 5. CREATE INTERNSHIPS
# ---------------------------------------------------------

internships = []

internship_id = 1

for student in students:

    student_id = student[0]
    cgpa = student[5]

    # Around 50% students get internships
    probability = 0.35

    if cgpa >= 8.0:
        probability = 0.60

    if random.random() < probability:

        internship_domain = random.choice([
            "Data Analytics",
            "Python Development",
            "Web Development",
            "Machine Learning",
            "Cloud Computing"
        ])

        duration = random.choice([
            "1 Month",
            "2 Months",
            "3 Months",
            "6 Months"
        ])

        internships.append([
            internship_id,
            student_id,
            internship_domain,
            duration
        ])

        internship_id += 1

save_csv(
    "internships.csv",
    [
        "internship_id",
        "student_id",
        "domain",
        "duration"
    ],
    internships
)


# ---------------------------------------------------------
# 6. CREATE PROJECTS
# ---------------------------------------------------------

projects = []

project_id = 1

project_names = [
    "Student Performance Dashboard",
    "E-Commerce Sales Analysis",
    "Smart Attendance System",
    "College Placement Predictor",
    "Library Management System",
    "Sign Language Recognition",
    "Campus Event Analytics",
    "Student Skill Analysis"
]

for student in students:

    student_id = student[0]
    cgpa = student[5]

    if cgpa >= 8.0:
        number_of_projects = random.randint(2, 4)
    elif cgpa >= 6.5:
        number_of_projects = random.randint(1, 3)
    else:
        number_of_projects = random.randint(1, 2)

    selected_projects = random.sample(
        project_names,
        number_of_projects
    )

    for project_name in selected_projects:

        technology = random.choice([
            "Python",
            "SQL",
            "Power BI",
            "HTML/CSS/JavaScript",
            "Machine Learning"
        ])

        projects.append([
            project_id,
            student_id,
            project_name,
            technology
        ])

        project_id += 1

save_csv(
    "projects.csv",
    [
        "project_id",
        "student_id",
        "project_name",
        "technology"
    ],
    projects
)


# ---------------------------------------------------------
# 7. CREATE PLACEMENT DATA
# ---------------------------------------------------------

placements = []

placement_id = 1

for student in students:

    student_id = student[0]
    cgpa = student[5]

    # Find attendance
    attendance_value = next(
        row[1]
        for row in attendance
        if row[0] == student_id
    )

    # Count skills
    skill_count = sum(
        1
        for row in student_skills
        if row[0] == student_id
    )

    # Check internship
    has_internship = any(
        row[1] == student_id
        for row in internships
    )

    # Count projects
    project_count = sum(
        1
        for row in projects
        if row[1] == student_id
    )

    # Placement score used only for our fictional dataset
    score = 0

    if cgpa >= 7.0:
        score += 25

    if cgpa >= 8.0:
        score += 10

    if attendance_value >= 75:
        score += 15

    if skill_count >= 4:
        score += 20
    elif skill_count >= 2:
        score += 10

    if has_internship:
        score += 15

    if project_count >= 2:
        score += 15

    # Add some randomness
    score += random.randint(-10, 10)

    # Decide placement
    placed = score >= 60

    if placed:

        company = random.choice(companies)

        company_id = company[0]

        package = round(
            random.uniform(3.5, 12.0),
            1
        )

        placements.append([
            placement_id,
            student_id,
            "Placed",
            company_id,
            company[1],
            package
        ])

    else:

        placements.append([
            placement_id,
            student_id,
            "Not Placed",
            "",
            "",
            0
        ])

    placement_id += 1


save_csv(
    "placements.csv",
    [
        "placement_id",
        "student_id",
        "placement_status",
        "company_id",
        "company_name",
        "package_lpa"
    ],
    placements
)


# ---------------------------------------------------------
# FINISHED
# ---------------------------------------------------------

print()
print("==========================================")
print("SMART CAMPUS DATA GENERATION COMPLETED!")
print("==========================================")
print("College: Sunrise Institute of Technology")
print("Students created: 1000")
print()
print("Check the DATA folder.")
print("Your CSV files are ready.")
print("==========================================")