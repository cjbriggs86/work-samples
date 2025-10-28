import random

def generate_random_assistivetechs(student_file = "studentdemographics.txt", assistivetech_file="iepassistivetechdevices.txt", num_devices_per_student=(1, 2)):

    """
    AssistiveTechID
    StudentID
    Student First Name
    Student Last Name
    Document Year
    Committee
    Device
    Quantity
    """

    try:
        with open(student_file, "r") as student_f:
            lines = student_f.readlines()[1:]  # Skip header
    except FileNotFoundError:
        print(f"Error: Student file '{student_file}' not found.")
        return

    types_doc_years = ["2023-2024", "2024-2025", "2025-2026"]
    types_doc_committees = ["CPSE", "CSE", "504"]
    types_devices = ["Wrist Stabilizer(s)", "Pencil Grips", "Velcro Pictureboard", "Crutches",
                     "Walker", "Nonmotorized Wheelchair", "Motorized Wheelchair", "Book Holder",
                     "Word Processer", "Visual Timer", "Automatic Page Turner", "Speech-to-Text Device",
                     "Text-to-Speech Device", "Eye-Gaze Interface", "Touch Screen Device"]
    types_quantities = [1, 2]
    assistivetech_data = []
    assistivetech_id = 100001

    for line in lines:
        student_data = line.strip().split("\t")
        if len(student_data) != 16: #Check if student file is properly formatted.
            print(f"Warning: Invalid data line in student file: {line.strip()}")
            continue
        student_id, first_name, last_name, _, _, _, _, _, _, _, _, _, _, _, _, _ = student_data

        num_devices = random.randint(num_devices_per_student[0], num_devices_per_student[1])

        for _ in range(num_devices):
            doc_year = random.choice(types_doc_years)
            doc_committee = random.choice(types_doc_committees)
            assistivetech = random.choice(types_devices)
            quantity = ""

            # set quantity to an appropriate value
            if assistivetech == "Wrist Stabilizer(s)":
                quantity = random.choice(types_quantities)
            elif assistivetech == "Pencil Grips":
                quantity = "6"
            elif assistivetech == "Crutches":
                quantity = "2"
            else:
                quantity = "1"

            assistivetech_data.append([
                assistivetech_id,
                student_id,
                first_name,
                last_name,
                doc_year,
                doc_committee,
                assistivetech,
                quantity
            ])
            assistivetech_id += 1

    headers = ["assistivetechID", "studentID", "firstname", "lastname", "year", "committee", "assistivetech", "quantity"]

    with open(assistivetech_file, "w") as program_v:
        program_v.write("\t".join(map(str, headers)) + "\n")
        for row in assistivetech_data:
            program_v.write("\t".join(map(str, row)) + "\n")

    print(f"Assistive Tech data written to '{assistivetech_file}' successfully.")

if __name__ == "__main__":
    generate_random_assistivetechs() #uses student file names, and 1-2 devices per student.