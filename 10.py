import mysql.connector
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )
def create_students_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            sex VARCHAR(10),
            rollno INT UNIQUE,
            marks INT
        )
    """)
    connection.commit()
    cursor.close()
def insert_rows(connection):
    cursor = connection.cursor()
    data_to_insert = [
        ("John Doe", "Male", 101, 85),
        ("Jane Doe", "Female", 102, 78),
        ("Bob Smith", "Male", 103, 92)
    ]
    cursor.executemany("""
        INSERT INTO students (name, sex, rollno, marks)
        VALUES (%s, %s, %s, %s)
    """, data_to_insert)
    connection.commit()
    cursor.close()
def update_marks(connection):
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE students
        SET marks = marks + 2
    """)
    connection.commit()
    cursor.close()
def delete_student(connection, rollno):
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM students
        WHERE rollno = %s
    """, (rollno,))
    connection.commit()
    cursor.close()
def display_student_details(connection, rollno):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT * FROM students
        WHERE rollno = %s
    """, (rollno,))
    student_details = cursor.fetchone()
    if student_details:
        print("Student Details:")
        print(f"Name: {student_details['name']}")
        print(f"Sex: {student_details['sex']}")
        print(f"Roll No: {student_details['rollno']}")
        print(f"Marks: {student_details['marks']}")
    else:
        print(f"No student found with Roll No: {rollno}")
    cursor.close()
if __name__ == "__main__":
    connection = create_connection()
    create_students_table(connection)
    insert_rows(connection)
    print("\nOriginal Student Details:")
    display_student_details(connection, 101)
    update_marks(connection)
    print("\nUpdated Student Details:")
    display_student_details(connection, 101)
    delete_student(connection, 102)
    print("\nStudent Details after Deletion:")
    display_student_details(connection, 102)
    connection.close()
