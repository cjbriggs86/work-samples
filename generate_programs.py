import random
import datetime

def generate_random_programs(student_file = "studentdemographics.txt", program_file="iepprograms.txt", num_programs_per_student=(1, 5)):

    """
    ProgramID
    StudentID
    Student First Name
    Student Last Name
    Document Year
    Committee
    Program
    Subject
    Program Start Date
    Program End Date
    Ratio
    Frequency
    Period
    """

    try:
        with open(student_file, "r") as student_f:
            lines = student_f.readlines()[1:]  # Skip header
    except FileNotFoundError:
        print(f"Error: Student file '{student_file}' not found.")
        return

    types_doc_years = ["2023-2024", "2024-2025", "2025-2026"]
    types_doc_committees = ["CPSE", "CSE", "504"]
    types_programs = ["Special Class", "Integrated Class", "Regular Class"]
    types_subjects = ["English", "Math", "Science", "Social Studies", "Spanish", "French", "Chinese", "Japanese",
                      "Arabic", "ASL", "German", "Italian", "Art", "Gym", "Music", "Chemistry",
                       "Biology", "Pre-Calculus"]
    types_ratios = ["1:1", "2:1", "3:1", "4:1", "5:1", "10:1", "12:1"]
    types_frequencies = [1, 2, 3, 4, 5, 6, 7, 8]
    types_periods = ["Daily", "Weekly", "Bi-Weekly", "2x Per Week", "3x Per Week", "Alternate Days", "Month", "Semester"]
    program_data = []
    program_id = 100001

    for line in lines:
        student_data = line.strip().split("\t")
        if len(student_data) != 16: #Check if student file is properly formatted.
            print(f"Warning: Invalid data line in student file: {line.strip()}")
            continue
        student_id, first_name, last_name, _, _, _, _, _, _, _, _, _, _, _, _, _ = student_data

        num_programs = random.randint(num_programs_per_student[0], num_programs_per_student[1])

        for _ in range(num_programs):
            doc_year = random.choice(types_doc_years)
            doc_committee = random.choice(types_doc_committees)
            program = random.choice(types_programs)
            subject = random.choice(types_subjects)
            ratio = random.choice(types_ratios)
            frequency = random.choice(types_frequencies)
            period = random.choice(types_periods)

            # ensures program dates correspond to random school year
            program_start = datetime.date(int(doc_year[0:4]), 9, 1)
            program_end = datetime.date(int(doc_year[5:]), 6, 30)

            program_data.append([
                program_id,
                student_id,
                first_name,
                last_name,
                doc_year,
                doc_committee,
                program,
                subject,
                program_start,
                program_end,
                ratio,
                frequency,
                period
            ])
            program_id += 1

    headers = ["programID", "studentID", "firstname", "lastname", "year", "committee", "program", "subject", "programstart", "programend",
               "ratio", "frequency", "period"]

    with open(program_file, "w") as program_v:
        program_v.write("\t".join(map(str, headers)) + "\n")
        for row in program_data:
            program_v.write("\t".join(map(str, row)) + "\n")

    print(f"Program data written to '{program_file}' successfully.")

if __name__ == "__main__":
    generate_random_programs() #uses default file names, and 1-5 programs per student.