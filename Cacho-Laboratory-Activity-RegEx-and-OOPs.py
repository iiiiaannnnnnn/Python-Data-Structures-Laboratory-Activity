import re
# PART 1 - REGULAR EXPRESSION TASKS

def extract_student_data(data):
    """Extract student information using regex with named groups."""
    pattern = r'ID:\s*(?P<id>\d{4}-\d{3})\s*\|\s*Name:\s*(?P<name>[A-Za-z\s]+)\s*\|\s*Email:\s*(?P<email>[^\s]+)\s*\|\s*Age:\s*(?P<age>\d+)'
    match = re.search(pattern, data)
    if match:
        return match.groupdict()
    return None

def validate_email(email):
    """Validate email format using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(pattern, email) is not None

def mask_email(email):
    """Mask the username part of an email."""
    pattern = r'^[^@]+'
    return re.sub(pattern, '*****', email)


def find_all_words(name):
    """Find all words in a name using regex."""
    return re.findall(r'[A-Za-z]+', name)

# PART 2 - PYTHON OOP TASKS

class Student:
    """Student class with basic attributes."""
    
    def __init__(self, student_id, name, email, age):
        """Constructor method to initialize student attributes."""
        self.student_id = student_id
        self.name = name

        self.__email = email
        self.__age = age

    def get_email(self):
        """Getter method for email."""
        return self.__email
    
    def set_email(self, email):
        """Setter method for email with validation."""
        if validate_email(email):
            self.__email = email
        else:
            raise ValueError("Invalid email format")
    

    def get_age(self):
        """Getter method for age."""
        return self.__age
    
    def set_age(self, age):
        """Setter method for age."""
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError("Invalid age")
    
    def display_info(self):
        """Display student information."""
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.__email}")
        print(f"Age: {self.__age}")

class Scholar(Student):
    """Scholar subclass that inherits from Student."""
    
    def __init__(self, student_id, name, email, age, scholarship_type):
        """Constructor that extends Student class."""
        super().__init__(student_id, name, email, age)
        self.scholarship_type = scholarship_type
    
    def display_scholar_info(self):
        """Display scholar information including scholarship type."""
        self.display_info()
        print(f"Scholarship: {self.scholarship_type}")

# PART 3 - INTEGRATION TASK (FINAL OUTPUT)

def validate_student_id(student_id):
    """Validate student ID format (YYYY-XXX)."""
    pattern = r'^\d{4}-\d{3}$'
    return re.match(pattern, student_id) is not None

def validate_name(name):
    """Validate that name contains only letters and spaces."""
    pattern = r'^[A-Za-z\s]+$'
    return re.match(pattern, name.strip()) is not None

def process_students(students_raw):
    """Process multiple student entries and create Student/Scholar objects."""
    student_records = []
    
    for entry in students_raw:
        data = extract_student_data(entry)
        
        if data:
            student_id = data['id']
            name = data['name'].strip()
            email = data['email']
            age = int(data['age'])
            
            if not validate_student_id(student_id):
                print(f"Invalid ID format: {student_id}")
                continue
            
            if not validate_name(name):
                print(f"Invalid name format: {name}")
                continue
            
            if not validate_email(email):
                print(f"Invalid email format: {email}")
                continue

            if "Scholarship:" in entry:
                scholarship_match = re.search(r'Scholarship:\s*(\w+)', entry)
                if scholarship_match:
                    scholarship_type = scholarship_match.group(1)
                    student = Scholar(student_id, name, email, age, scholarship_type)
                else:
                    student = Student(student_id, name, email, age)
            else:
                student = Student(student_id, name, email, age)
            
            student_records.append(student)
        else:
            print(f"Failed to extract data from: {entry}")
    
    return student_records

# MAIN PROGRAM - DEMONSTRATION


if __name__ == "__main__":
    print("STUDENT INFORMATION PROCESSING SYSTEM")

    print()
    

    students_raw = [
        "ID: 2025-001 | Name: Juan Dela Cruz | Email: juan.cruz@example.com | Age: 20",
        "ID: 2025-002 | Name: Maria Santos | Email: maria.santos@school.edu | Age: 21 | Scholarship: Academic",
        "ID: 2025-003 | Name: Pedro Reyes | Email: pedro.reyes@university.ph | Age: 22",
        "ID: 2025-004 | Name: Ana Gonzales | Email: ana.gonzales@school.edu | Age: 19 | Scholarship: Athletic"
    ]
    
    print("Processing student records...\n")
    

    student_records = process_students(students_raw)
    
    print(f"Successfully processed {len(student_records)} student(s)\n")
    print("=" * 70)
    print()
    

    for i, student in enumerate(student_records, 1):
        if isinstance(student, Scholar):
            student.display_scholar_info()
        else:
            student.display_info()
        
        if i < len(student_records):
            print("-" * 70)
            print()
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION OF SPECIFIC TASKS")
    print("=" * 70)
    print()
    

    print("Task 3 - Email Masking:")
    sample_email = "juan.cruz@example.com"
    print(f"Original: {sample_email}")
    print(f"Masked: {mask_email(sample_email)}")
    print()
    

    print("Task 4 - Find All Words in Name:")
    sample_name = "Juan Dela Cruz"
    words = find_all_words(sample_name)
    print(f"Name: {sample_name}")
    print(f"Words: {words}")
    print()
    

    print("Task 6 - Email Validation via Setter:")
    test_student = student_records[0]
    print(f"Current email: {test_student.get_email()}")
    try:
        test_student.set_email("newemail@valid.com")
        print(f"Updated email: {test_student.get_email()}")
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        test_student.set_email("invalid-email")
        print(f"Updated email: {test_student.get_email()}")
    except ValueError as e:
        print(f"Error updating to invalid email: {e}")
    
    print("\n" + "=" * 70)
    print("PROGRAM COMPLETED SUCCESSFULLY")
    print("=" * 70)