import mysql.connector
import pandas as pd

print("1 - Python started")

try:
    # Connect to MySQL
    db = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root@2026!@#",
        database="smart_maha_campus",
        connection_timeout=5,
        use_pure=True
    )
    cursor =db.cursor()
    print("2 - Database connected successfully!")

    # Read student data
    students = pd.read_sql(
        "SELECT * FROM students",
        db
    )
    print("\n3 - Student data loaded successfully!")
    print(students.head())

    # Number of students
    print("\n4 - Total students:", len(students))
    
    print("checking placements..",flush=True)
    
    cursor.execute("SELECT COUNT(*) FROM placements")
    placements = cursor.fetchone()[0]
    print("Total Placements:", placements, flush=True)
    
    placement_percentage = (placements / len(students)) * 100
    print("Placement Percentage:", round(placement_percentage, 2), "%", flush=True)
    not_placed = len(students) - placements
    print("Students Placed:", placements, flush=True)
    print("Students Not Placed:", not_placed, flush=True)
    not_placed_percentage = (not_placed / len(students)) * 100
    print("Not Placed Percentage:", round(not_placed_percentage, 2), "%", flush=True)
    
    
    cursor.execute("SELECT COUNT(*) FROM projects")
    projects = cursor.fetchone()[0]
    
    print("Checking projects...", flush=True)
    print("Total Projects:", projects, flush=True)
    average_projects = projects / len(students)
    print("Average Projects per Student:", round(average_projects, 2), flush=True)
    projects_per_placed_student = projects / placements
    print("Projects per Placed Student:", round(projects_per_placed_student, 2), flush=True)
    cursor.execute("SELECT AVG(package_lpa) FROM placements")
    average_package = cursor.fetchone()[0]
    print("Average Package:", round(average_package, 2), "LPA", flush=True)
    cursor.execute("SELECT COUNT(DISTINCT company_name) FROM placements")
    companies = cursor.fetchone()[0]
    print("Companies with Placements:", companies, flush=True)
    cursor.execute("SELECT MAX(package_lpa) FROM placements")
    highest_package = cursor.fetchone()[0]
    print("Highest Package:", highest_package, "LPA", flush=True) 
    cursor.execute("SELECT MIN(package_lpa) FROM placements")
    lowest_package = cursor.fetchone()[0]
    print("Lowest Package:", lowest_package, "LPA", flush=True)
    cursor.execute("SELECT SUM(package_lpa) FROM placements")
    total_package = cursor.fetchone()[0]
    print("Total Package Value:", round(total_package, 2), "LPA", flush=True)
    cursor.execute("""
    SELECT company_name, COUNT(*) AS placement_count
    FROM placements
    GROUP BY company_name
    ORDER BY placement_count DESC
    LIMIT 1
    """)

    top_company = cursor.fetchone()

    print("Top Placement Company:", top_company[0], flush=True)
    print("Students Placed by Top Company:", top_company[1], flush=True)
    cursor.execute("""
    SELECT company_name, COUNT(*) AS placement_count
    FROM placements
    GROUP BY company_name
    ORDER BY placement_count DESC
    """)

    company_data = cursor.fetchall()

    print("Company-wise Placements:", flush=True)

    for company, count in company_data:
      print(company, ":", count, flush=True)
    cursor.execute("""
    SELECT company_name, ROUND(AVG(package_lpa), 2) AS average_package
    FROM placements
    GROUP BY company_name
    ORDER BY average_package DESC
    """)

    company_package_data = cursor.fetchall()

    print("Company-wise Average Package:", flush=True)

    for company, package in company_package_data:
     print(company, ":", package, "LPA", flush=True)
    cursor.execute("""
    SELECT COUNT(DISTINCT company_name)
    FROM placements
    """)

    unique_companies = cursor.fetchone()[0]

    print("Total Unique Companies:", unique_companies, flush=True)
    print("\n========== CAMPUS ANALYTICS SUMMARY ==========")
    print("Total Students:", students)
    print("Students Placed:", placements)
    print("Students Not Placed:", not_placed)
    print("Placement Percentage:", round(placement_percentage, 2), "%")
    print("Not Placed Percentage:", round(not_placed_percentage, 2), "%")
    print("Total Projects:", projects)
    print("Average Projects per Student:", round(average_projects, 2))
    print("Average Package:", round(average_package, 2), "LPA")
    print("Highest Package:", highest_package, "LPA")
    print("Lowest Package:", lowest_package, "LPA")
    print("Total Unique Companies:", unique_companies)
    print("==============================================")
    
    cursor.close()
    db.close()
    print("\n5 - Connection closed")
    print("Analysis completed successfully!")
    
except Exception as e:
    print("\nERROR:")
    print(e)
    
    