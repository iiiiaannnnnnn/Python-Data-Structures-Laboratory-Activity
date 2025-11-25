# Task 2.1: Coordinate System with Tuples
import math

def calculate_distance(point1, point2):
    """Calculate distance between two points"""
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def find_midpoint(point1, point2):
    """Find midpoint between two points"""
    x1, y1 = point1
    x2, y2 = point2
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
    return midpoint

# Task 2.2: Unique Word Counter with Sets
def count_unique_words(text):
    """Count unique words in text"""
    words = text.lower().replace('.', '').replace(',', '').split()
    
    unique_words = set(words)

    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    print("\n" + "="*40)
    print("TASK 2.2: Unique Word Counter")
    print("="*40)
    print(f"Original text: {text}")
    print(f"\nTotal words: {len(words)}")
    print(f"Unique words: {len(unique_words)}")
    print(f"\nUnique words: {sorted(unique_words)}")

    most_common = max(word_freq.items(), key=lambda x: x[1])
    print(f"\nMost common word: '{most_common[0]}' (appears {most_common[1]} times)")
    
    print("\nWord frequencies:")
    for word, count in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print(f"  {word}: {count}")


if __name__ == "__main__":
    print("="*40)
    print("TASK 2.1: Coordinate System")
    print("="*40)
    

    point1 = (2, 3)
    point2 = (5, 7)
    point3 = (1, 1)
    

    all_points = (point1, point2, point3)
    
    print(f"Point 1: {point1}")
    print(f"Point 2: {point2}")
    print(f"Point 3: {point3}")
    

    dist = calculate_distance(point1, point2)
    print(f"\nDistance between {point1} and {point2}: {dist:.2f}")
    

    mid = find_midpoint(point1, point2)
    print(f"Midpoint between {point1} and {point2}: {mid}")
    

    print("\n" + "="*40)
    print("Demonstrating Tuple Immutability")
    print("="*40)
    print(f"Trying to modify point1: {point1}")
    try:
        point1[0] = 10  
    except TypeError as e:
        print(f"Error: {e}")
        print("Tuples are immutable - cannot be modified!")
    
    sample_text = "Python is a programming language. Python is easy to learn. Python is powerful."
    count_unique_words(sample_text)