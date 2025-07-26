def check_attendance_eligibility():
    total_working_days = int(input("Enter the total number of working days: "))
    total_days_absent = int(input("Enter the total number of days absent: "))
    
    attendance_percentage = ((total_working_days - total_days_absent) / total_working_days) * 100
    
    print(f"Attendance Percentage: {attendance_percentage:.2f}%")
    
    if attendance_percentage >= 75:
        print("The student is eligible to sit for the exam.")
    else:
        print("The student is not eligible to sit for the exam.")

if __name__ == "__main__":
    check_attendance_eligibility()