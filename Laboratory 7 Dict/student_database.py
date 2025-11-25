# Task 3.1: Student Database using Dictionaries

students = {}

def add_student(student_id, name, grade, major):
    """Add a student with ID, name, grade, and major"""
    students[student_id] = {
        'name': name,
        'grade': grade,
        'major': major
    }
    print(f"Added student: {name} (ID: {student_id})")

def get_student(student_id):
    """Retrieve student information by ID"""
    if student_id in students:
        return students[student_id]
    else:
        return None

def update_grade(student_id, new_grade):
    """Update a student's grade"""
    if student_id in students:
        old_grade = students[student_id]['grade']
        students[student_id]['grade'] = new_grade
        print(f"Updated {students[student_id]['name']}'s grade from {old_grade} to {new_grade}")
    else:
        print(f"Student ID {student_id} not found!")

def display_all_students():
    """Display all students"""
    print("\n" + "="*50)
    print("ALL STUDENTS")
    print("="*50)
    if not students:
        print("No students in database.")
    else:
        for student_id, info in students.items():
            print(f"ID: {student_id}")
            print(f"  Name: {info['name']}")
            print(f"  Grade: {info['grade']}")
            print(f"  Major: {info['major']}")
            print("-" * 50)

# Task 3.2: Word Frequency Counter
def count_word_frequency(text):
    """Count word frequencies in text"""
    print("\n" + "="*50)
    print("TASK 3.2: Word Frequency Counter")
    print("="*50)
    
    text = text.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    words = text.split()
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    print(f"Original text: {text}")
    print(f"\nTotal words: {len(words)}")
    print(f"Unique words: {len(word_count)}")
    
    print("\nWord frequencies (sorted by count):")
    for word, count in sorted_words:
        print(f"  '{word}': {count}")
    
    most_common = sorted_words[0]
    print(f"\nMost common word: '{most_common[0]}' appears {most_common[1]} times")

if __name__ == "__main__":
    print("="*50)
    print("TASK 3.1: Student Database")
    print("="*50)
    
    add_student("S001", "Alice Johnson", "A", "Computer Science")
    add_student("S002", "Bob Smith", "B+", "Engineering")
    add_student("S003", "Charlie Brown", "A-", "Mathematics")
    
    display_all_students()
    
    print("\n" + "="*50)
    print("RETRIEVING STUDENT S002")
    print("="*50)
    student = get_student("S002")
    if student:
        print(f"Name: {student['name']}")
        print(f"Grade: {student['grade']}")
        print(f"Major: {student['major']}")
    

    print("\n" + "="*50)
    print("UPDATING GRADE")
    print("="*50)
    update_grade("S002", "A")
    
    display_all_students()
    
    # Task 3.2: Word Frequency Counter
    sample_text = "Python is amazing. Python makes programming easy. Programming with Python is fun."
    count_word_frequency(sample_text)