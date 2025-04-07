def create_student_dict():
    student_dict = {}
    num_students = int(input("Enter the number of students: "))
    
    for _ in range(num_students):
        name = input("Enter the name of the student: ")
        subjects = {}
        num_subjects = int(input(f"Enter the number of subjects for {name}: "))
        
        for _ in range(num_subjects):
            subject = input("Enter the name of the subject: ")
            mark = float(input(f"Enter the mark for {subject}: "))
            subjects[subject] = mark
        
        student_dict[name] = subjects
    
    return student_dict


if __name__ == "__main__":
    student_marks = create_student_dict()
    print("\nStudent Mark Dictionary")
    
    for student, subjects in student_marks.items():
        print(f"\n{student}:")
        for subject, mark in subjects.items():
            print(f"{subject}: {mark}")
