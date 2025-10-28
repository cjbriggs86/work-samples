import random
import datetime

def generate_random_reportcards(student_file = "studentdemographics.txt", reportcard_file="reportcards.txt"):

    # OUTPUT FILE FORMAT
    """
    ReportID
    School Year
    StudentID
    Student First Name
    Student Last Name
    Native Language
    Classification
    Is Special Ed
    Committee
    Marking Period
    Class
    Grade
    """

    # Validate studentdemographics.txt
    try:
        with open(student_file, "r") as student_f:
            lines = student_f.readlines()[1:]  # Skip header
    except FileNotFoundError:
        print(f"Error: Student file '{student_file}' not found.")
        return
    
    # Variable values
    types_coreclasses = ["English", "Math", "Science", "Social Studies", "Gym"]
    types_foreignlanguages = ["Spanish", "French", "Italian", "Japanese"]
    types_electives = ["Art", "Music", "Computer Science", "Journalism", "Business Administration", "FACS"]
    
    reportcard_data = []
    reportcard_id = 1001

    for line in lines:
        student_data = line.strip().split("\t")
        if len(student_data) != 17: #Check if student file is properly formatted.
            print(f"Warning: Invalid data line in student file: {line.strip()}")
            continue
        student_id, first_name, last_name, _, _, native_language, classification, _, _, _, _, _, _, _, _, _ = student_data


        for _ in range(types_coreclasses):
            school_year = "2023-2024" # Hardcoded for testing in Q2 2025
            studentid = student_id
            firstname = first_name
            lastname = last_name

            # Correlate Classification and Committee
            spec_ed = None
            if classification == "General Education":
                spec_ed = "Yes"
            else: spec_ed = "No"

            committee = None
            if classification == []:
                committee = "CSE"
            elif classification == []:
                committee = "504"
            else: committee = "General Education"

            # Loop through Marking Periods 1 - 4 per student
            markingperiod = 1

            # Loop through Classes per student
            sched_class = None

            # Assign random grades
            mp_grade = random.random()

            # Correlate letter grades
            letter_grade = None
            if mp_grade <= 0.65: letter_grade = "F"
            elif mp_grade >= 0.65: letter_grade = "D"
            elif mp_grade >= 0.7: letter_grade = "C"
            elif mp_grade >= 0.8: letter_grade = "B"
            elif mp_grade >= 0.9: letter_grade = "A"


            reportcard_data.append([
                reportcard_id,
                school_year,
                studentid,
                firstname,
                lastname,
                native_language,
                classification,
                committee,
                spec_ed,                
                markingperiod,
                sched_class,
                mp_grade,
                letter_grade
            ])
            reportcard_id += 1

    headers = ["reportcardID", "schoolyear", "studentID", "firstname", "lastname", "nativelanguage", "classification",
               "committee", "spec_ed", "program", "subject", "programstart", "programend",
               "ratio", "frequency", "period"]

    with open(reportcard_file, "w") as reportcards_v:
        reportcards_v.write("\t".join(map(str, headers)) + "\n")
        for row in reportcard_data:
            reportcards_v.write("\t".join(map(str, row)) + "\n")

    print(f"Report Card data written to '{reportcard_file}' successfully.")

if __name__ == "__main__":
    generate_random_reportcards() #uses default file names, and 1-5 programs per student.