# Student Contact Database

students = {
    101: "rahul@example.com",
    102: "priya@example.com",
    103: "amit@example.com",
    104: "sneha@example.com"
}

roll_id = int(input("Enter student roll number: "))

if roll_id in students:
    print(f"Email address: {students[roll_id]}")
else:
    print("Student roll number not found.")