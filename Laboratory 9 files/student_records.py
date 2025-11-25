# Task 4.1: Student Records File System
import pickle

def save_records(records, filename="students.pkl"):
    """Save student records using pickle"""
    try:
        with open(filename, 'wb') as file:
            pickle.dump(records, file)
        print(f" Records saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving records: {e}")
        return False

def load_records(filename="students.pkl"):
    """Load student records from pickle file"""
    try:
        with open(filename, 'rb') as file:
            records = pickle.load(file)
        print(f" Records loaded from {filename}")
        return records
    except FileNotFoundError:
        print(f"Error: File {filename} not found!")
        return None
    except Exception as e:
        print(f"Error loading records: {e}")
        return None

def export_to_text(records, filename="students.txt"):
    """Export student records to a readable text file"""
    try:
        with open(filename, 'w') as file:
            file.write("="*60 + "\n")
            file.write("STUDENT RECORDS\n")
            file.write("="*60 + "\n\n")
            
            for student_id, info in records.items():
                file.write(f"Student ID: {student_id}\n")
                file.write(f"  Name: {info['name']}\n")
                file.write(f"  Grade: {info['grade']}\n")
                file.write(f"  Major: {info['major']}\n")
                file.write("-"*60 + "\n")
        
        print(f" Records exported to {filename}")
        return True
    except Exception as e:
        print(f"Error exporting records: {e}")
        return False

# Task 4.2: File Operations Practice
def demonstrate_file_operations():
    """Demonstrate different file modes"""
    print("\n" + "="*60)
    print("TASK 4.2: File Operations Practice")
    print("="*60)
    
    print("\n1. Writing to a new file (w mode)...")
    try:
        with open("sample.txt", 'w') as file:
            file.write("This is line 1\n")
            file.write("This is line 2\n")
            file.write("This is line 3\n")
        print(" File written successfully")
    except Exception as e:
        print(f"Error writing file: {e}")
    
    print("\n2. Reading from a file (r mode)...")
    try:
        with open("sample.txt", 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("Error: File not found!")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    print("3. Appending to a file (a mode)...")
    try:
        with open("sample.txt", 'a') as file:
            file.write("This is line 4 (appended)\n")
            file.write("This is line 5 (appended)\n")
        print(" Content appended successfully")
    except Exception as e:
        print(f"Error appending to file: {e}")
    
    print("\n4. Reading file again to show appended content...")
    try:
        with open("sample.txt", 'r') as file:
            content = file.read()
            print("Updated file contents:")
            print(content)
    except Exception as e:
        print(f"Error reading file: {e}")
    
    print("5. Demonstrating file not found error handling...")
    try:
        with open("nonexistent.txt", 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(" Handled FileNotFoundError: The file does not exist")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("="*60)
    print("TASK 4.1: Student Records File System")
    print("="*60)
    
    student_records = {
        "S001": {
            "name": "Alice Johnson",
            "grade": "A",
            "major": "Computer Science"
        },
        "S002": {
            "name": "Bob Smith",
            "grade": "B+",
            "major": "Engineering"
        },
        "S003": {
            "name": "Charlie Brown",
            "grade": "A-",
            "major": "Mathematics"
        }
    }
    
    print("\nOriginal student records:")
    for sid, info in student_records.items():
        print(f"{sid}: {info['name']} - {info['grade']} - {info['major']}")
    
    print("\n" + "-"*60)
    save_records(student_records)
    
    print("\n" + "-"*60)
    loaded_records = load_records()
    
    if loaded_records:
        print("\nLoaded student records:")
        for sid, info in loaded_records.items():
            print(f"{sid}: {info['name']} - {info['grade']} - {info['major']}")
    
    print("\n" + "-"*60)
    export_to_text(student_records)
    
    print("\n Check 'students.txt' to see the readable export")
    
    demonstrate_file_operations()
    
    print("\n" + "="*60)
    print("ALL TASKS COMPLETED!")
    print("="*60)
    print("\nFiles created:")
    print("  - students.pkl (pickle file)")
    print("  - students.txt (readable export)")
    print("  - sample.txt (file operations demo)")