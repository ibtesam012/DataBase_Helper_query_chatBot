import sqlite3
conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")
conn.commit()
# Insert sample data only if table is empty
cursor.execute("SELECT COUNT(*) FROM employees")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
        [
            ("Alice", "HR", 50000),
            ("Bob", "Engineering", 80000),
            ("Carol", "Marketing", 60000),
            ("David", "Engineering", 90000),
        ]
    )
    conn.commit()
    print("Sample data inserted.")

print("=== Database Query Helper Chatbot ===")
while True:
    user_input = input("\nAsk a question (or type exit): ")
    if user_input.lower() == "exit":
        break
    if "all employees" in user_input.lower():
        cursor.execute("SELECT * FROM employees")
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No records found.")
    elif "employee count" in user_input.lower():
        cursor.execute("SELECT COUNT(*) FROM employees")
        print("Total Employees:", cursor.fetchone()[0])
    else:
        print("Sorry, I don't understand that query yet.")

conn.close()