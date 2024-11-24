import os
import matplotlib.pyplot as plt

# Load students data
def load_students(file_path):
    """Load student data into a dictionary."""
    students = {}
    with open(file_path, 'r') as file:
        for line in file:
            student_id, student_name = line.strip()[:3], line.strip()[3:]
            students[student_id] = student_name
    return students


# Load assignments data
def load_assignments(file_path):
    """Load assignment data into a dictionary."""
    assignments = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):  # Process in chunks of 3 lines
            assignment_name = lines[i].strip()
            assignment_id = lines[i + 1].strip()
            assignments[assignment_id] = assignment_name
    return assignments


# Load submissions data
def load_submissions(folder_path):
    """Load submissions into a dictionary grouped by assignment ID."""
    submissions = {}
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            for line in file:
                student_id, assignment_id, score = line.strip().split('|')
                score = float(score)
                if assignment_id not in submissions:
                    submissions[assignment_id] = []
                submissions[assignment_id].append(score)
    return submissions


# Calculate statistics for an assignment
def assignment_statistics(assignments, submissions, assignment_name):
    """Print statistics for an assignment."""
    # Find the assignment ID for the given name
    assignment_id = None
    for aid, name in assignments.items():
        if name == assignment_name:
            assignment_id = aid
            break

    if not assignment_id or assignment_id not in submissions:
        print("Assignment not found")
        return

    # Get all scores for the assignment
    scores = submissions[assignment_id]

    if scores:
        min_score = min(scores)
        max_score = max(scores)
        avg_score = sum(scores) / len(scores)

        print(f"Min: {round(min_score)}%")
        print(f"Avg: {round(avg_score)}%")
        print(f"Max: {round(max_score)}%")
    else:
        print("No submissions found for this assignment")


# Plot histogram for an assignment
def assignment_graph(assignments, submissions, assignment_name):
    """Display a histogram for an assignment."""
    # Find the assignment ID for the given name
    assignment_id = None
    for aid, name in assignments.items():
        if name == assignment_name:
            assignment_id = aid
            break

    if not assignment_id or assignment_id not in submissions:
        print("Assignment not found")
        return

    # Get all scores for the assignment
    scores = submissions[assignment_id]
    plt.hist(scores, bins=[50, 60, 70, 80, 90, 100], edgecolor='black', color='blue')
    plt.title(f"Histogram for {assignment_name}")
    plt.xlabel("Score Ranges")
    plt.ylabel("Frequency")
    plt.show()


# Main menu
def main_menu():
    print("Menu")
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    choice = input("Enter your selection: ")

    if choice == "1":
        student_name = input("What is the student's name: ")
        calculate_student_grade(students, submissions, student_name)
    elif choice == "2":
        assignment_name = input("What is the assignment name: ")
        assignment_statistics(assignments, submissions, assignment_name)
    elif choice == "3":
        assignment_name = input("What is the assignment name: ")
        assignment_graph(assignments, submissions, assignment_name)
    else:
        print("Invalid selection")


# Paths to files
# Relative paths for the script to locate files in the same directory
students_file_path = './students.txt'
assignments_file_path = './assignments.txt'
submissions_folder_path = './submissions'


# Load data
students = load_students(students_file_path)
assignments = load_assignments(assignments_file_path)
submissions = load_submissions(submissions_folder_path)

# Run the program
main_menu()
