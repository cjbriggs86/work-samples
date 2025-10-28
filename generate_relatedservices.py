import random
import datetime

def generate_random_relatedservices(student_file = "studentdemographics.txt", relatedservice_file="ieprelatedservices.txt", num_services_per_student=(1, 5)):

    """
    RelatedServiceID
    StudentID
    Student First Name
    Student Last Name
    Document Year
    Committee
    Service
    Related Service Start Date
    Related Service End Date
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
    types_doc_committees = ["CPSE", "CSE"]
    types_relatedservices = ["Speech-Language Therapy", "Audiology", "Interpreter", "Psychological Services",
                             "Physical Therapy", "Occupational Therapy", "Counseling", "Orientation and/or Mobility",
                             "Parent Counseling and/or Training", "School Nurse Services", "Assistive Technology Training",
                             "Therapeutic Recreation"]
    types_frequencies = [1, 2, 3, 4, 5, 6, 7, 8]
    types_periods = ["Daily", "Weekly", "Bi-Weekly", "2x Per Week", "3x Per Week", "Alternate Days", "Month", "Semester"]
    relatedservices_data = []
    relatedservice_id = 100001

    for line in lines:
        student_data = line.strip().split("\t")
        if len(student_data) != 17: #Check if student file is properly formatted.
            print(f"Warning: Invalid data line in student file: {line.strip()}")
            continue
        student_id, first_name, last_name, _, _, _, _, _, _, _, _, _, _, _, _, _, _ = student_data

        num_relatedservices = random.randint(num_services_per_student[0], num_services_per_student[1])

        for _ in range(num_relatedservices):
            doc_year = random.choice(types_doc_years)
            doc_committee = random.choice(types_doc_committees)
            relatedservice = random.choice(types_relatedservices)
            frequency = random.choice(types_frequencies)
            period = random.choice(types_periods)

            # ensures program dates correspond to random school year
            relatedservice_start = datetime.date(int(doc_year[0:4]), 9, 1)
            relatedservice_end = datetime.date(int(doc_year[5:]), 6, 30)

            relatedservices_data.append([
                relatedservice_id,
                student_id,
                first_name,
                last_name,
                doc_year,
                doc_committee,
                relatedservice,
                relatedservice_start,
                relatedservice_end,
                frequency,
                period
            ])
            relatedservice_id += 1

    headers = ["relatedserviceID", "studentID", "firstname", "lastname", "year", "committee", "relatedservice",
               "relatedservicestart", "relateserviceend", "frequency", "period"]

    with open(relatedservice_file, "w") as program_v:
        program_v.write("\t".join(map(str, headers)) + "\n")
        for row in relatedservices_data:
            program_v.write("\t".join(map(str, row)) + "\n")

    print(f"Program data written to '{relatedservice_file}' successfully.")

if __name__ == "__main__":
    generate_random_relatedservices() #uses default file names, and 1-5 programs per student.