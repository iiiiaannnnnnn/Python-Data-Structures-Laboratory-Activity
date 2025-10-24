# Task 1.1: Student Grade Manager

student_names = []
student_grades = []

def add_student(name, grade):
    """Add a student and their grade"""
    student_names.append(name)
    student_grades.append(grade)
    print(f"Added {name} with grade {grade}")

def calculate_average():
    """Calculate average grade"""
    if len(student_grades) == 0:
        return 0
    return sum(student_grades) / len(student_grades)

def find_highest():
    """Find the highest grade"""
    if len(student_grades) == 0:
        return 0
    return max(student_grades)

def display_all():
    """Display all students and their grades"""
    print("\nStudent Grades:")
    for i in range(len(student_names)):
        print(f"{student_names[i]}: {student_grades[i]}")
    print(f"\nAverage Grade: {calculate_average()}")
    print(f"Highest Grade: {find_highest()}")

# Task 1.2: List Operations Practice
def list_operations():
    """Practice various list operations"""
    numbers = [5, 2, 8, 1, 9, 3]
    print("\n" + "="*40)
    print("TASK 1.2: List Operations")
    print("="*40)
    print(f"Original list: {numbers}")
    
    sorted_numbers = sorted(numbers)
    print(f"Sorted list: {sorted_numbers}")

    total = sum(numbers)
    print(f"Sum: {total}")
    

    average = sum(numbers) / len(numbers)
    print(f"Average: {average}")
    
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
    
    print(f"Length: {len(numbers)}")

if __name__ == "__main__":
    print("="*40)
    print("TASK 1.1: Student Grade Manager")
    print("="*40)
    

    add_student("Alice", 85)
    add_student("Bob", 92)
    add_student("Charlie", 78)
    

    display_all()

    list_operations()