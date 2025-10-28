import random

def create_assignments(student_file="studentdemographics.txt", admin_file="administrators.txt", assignment_file="studentassignments.txt"):
    """
    Creates a file with random assignments of students to administrators.

    Args:
        student_file: Path to the student demographics file.
        admin_file: Path to the administrators file.
        assignment_file: Path to the output assignment file.
    """
    try:
        with open(student_file, "r") as f:
            student_ids = [line.strip().split('\t')[0] for line in f.readlines()[1:] if line.strip()]  # Extract student IDs
    except FileNotFoundError:
        print(f"Error: Student file '{student_file}' not found.  Please create this file with student data.")
        return

    try:
        with open(admin_file, "r") as f:
            admin_ids = [line.strip().split('\t')[0] for line in f.readlines()[1:] if line.strip()]  # Extract administrator IDs
    except FileNotFoundError:
        print(f"Error: Administrator file '{admin_file}' not found. Please create this file with administrator data.")
        return

    if not student_ids:
        print(f"Error: No student IDs found in '{student_file}'.")
        return
    if not admin_ids:
        print(f"Error: No administrator IDs found in '{admin_file}'.")
        return

    types_schoolyears = ["2023-2024", "2024-2025", "2025-2026"]
    types_actives = [True, False]
    assignmentid = 10001

    assignments = []
    for student_id in student_ids:
        #  randomly assign one administrator per student.
        admin_id = random.choice(admin_ids)
        schoolyear = random.choice(types_schoolyears)
        isactive = random.choice(types_actives)
        
        assignments.append((assignmentid, student_id, admin_id, schoolyear, isactive))
        assignmentid += 1

    with open(assignment_file, "w") as f:
        f.write("assignmentid\tstudentID\tadminID\tschoolyear\risactive\n")
        for assignmentid, student_id, admin_id, schoolyear, isactive in assignments:
            f.write(f"{assignmentid}\t{student_id}\t{admin_id}\t{schoolyear}\t{isactive}\n")

    print(f"Assignments written to '{assignment_file}' successfully.")

if __name__ == "__main__":
    create_assignments()
