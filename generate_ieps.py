import random
import datetime

def generate_iep_documents(student_file = "studentdemographics.txt", user_file = "users.txt", generate_ieps = "iepdocuments.txt", number_ieps=(1,3)):

    """
        Reads student data, generates contact info, and writes to a new tab-delimited file.

    Args:
        student_file: Path to the student data file.
        user_file: Path to the user data file.
        generate_ieps: Path to the output IEP Documents file.
        number_ieps: Tuple specifying the range of IEP Documents per student.

    Output file format:
    Document ID
    Student ID
    Student First Name
    Student Last Name
    School Year
    Committee
    Is Original
    Created By
    Created Date
    Is Finalized
    Finalized Date
    """

    try:
        with open(student_file, "r") as student_f:
            lines = student_f.readlines()[1:]  # Skip header
    except FileNotFoundError:
        print(f"Error: Student file '{student_file}' not found.")
        return

    types_doc_years = ["2023-2024", "2024-2025", "2025-2026"]
    types_doc_committees = ["CPSE", "CSE", "504"]
    document_data = []
    document_id = 1001

    for line in lines:
        student_data = line.strip().split("\t")
        if len(student_data) != 16: #Check if student file is properly formatted.
            print(f"Warning: Invalid data line in student file: {line.strip()}")
            continue
        student_id, first_name, last_name, _, _, _, _, _, _, _, _, _, _, _, _, _ = student_data

        num_IEPs = random.randint(number_ieps[0], number_ieps[1])

        for _ in range(num_IEPs):
            doc_year = random.choice(types_doc_years)
            doc_committee = random.choice(types_doc_committees)
            
            # ensures created and finalized dates correspond to random school year
            doc_created_date = datetime.date(int(doc_year[0:4]), 7, 1)
            doc_finalized_date = datetime.date(int(doc_year[5:]), 8, 1)

            is_original = random.choice(["True", "False"])
            is_finalized = random.choice(["True", "False"])

            if is_finalized == "False": doc_finalized_date = ""

            document_data.append([
                document_id,
                student_id,
                first_name,
                last_name,
                doc_year,
                doc_committee,
                is_original,
                doc_created_date,
                is_finalized,
                doc_finalized_date
            ])
            document_id += 1

    headers = ["documentID", "studentID", "firstname", "lastname", "doc_year", "doc_committee",
               "is_original", "created_date", "is_finalized", "finalized_date"]

    with open(generate_ieps, "w") as program_v:
        program_v.write("\t".join(map(str, headers)) + "\n")
        for row in document_data:
            program_v.write("\t".join(map(str, row)) + "\n")

    print(f"IEP data written to '{generate_ieps}' successfully.")

if __name__ == "__main__":
    generate_iep_documents() #uses default file names, and 1-5 programs per student.