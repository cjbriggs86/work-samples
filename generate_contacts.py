import random

def create_contacts(student_file="studentdemographics.txt", contact_file="contact_data.txt", num_contacts_per_student=(1, 3)):
    """
    Reads student data, generates contact info, and writes to a new tab-delimited file.

    Args:
        student_file: Path to the student data file.
        contact_file: Path to the output contact file.
        num_contacts_per_student: Tuple specifying the range of contacts per student.
    """

    try:
        with open(student_file, "r") as student_f:
            lines = student_f.readlines()[1:]  # Skip header
    except FileNotFoundError:
        print(f"Error: Student file '{student_file}' not found.")
        return

    relationships = ["Mother", "Father", "Parent", "Legal Guardian", "Brother", "Sister", "Aunt", "Uncle", "Grandmother", "Grandfather", "Grandparent", "Foster Mother", "Foster Father", "Foster Parent"]
    contact_data = []
    contact_id = 100001

    for line in lines:
        student_data = line.strip().split("\t")
        if len(student_data) != 16: #Check if student file is properly formed.
            print(f"Warning: Invalid data line in student file: {line.strip()}")
            continue
        student_id, _, last_name, _, _, native_language, home_street, home_street2, home_city, home_state, home_zip, mail_street, mail_street2, mail_city, mail_state, mail_zip = student_data

        num_contacts = random.randint(num_contacts_per_student[0], num_contacts_per_student[1])

        for _ in range(num_contacts):
            relationship = random.choice(relationships)
            send_mail = random.choice([True, False])
            first_name = random.choice(["John", "Jane", "Robert", "Mary", "Michael", "Jennifer", "William", "Linda", "David", "Susan", "Apple", "Betty", "Carmichael", "George", "Henrietta", "Lupita", "Consuela", "Tio", "Tia", "Klondike"])

            contact_data.append([
                contact_id,
                student_id,
                first_name,
                last_name,
                relationship,
                native_language,
                home_street,
                home_street2,
                home_city,
                home_state,
                home_zip,
                mail_street,
                mail_street2,
                mail_city,
                mail_state,
                mail_zip,
                send_mail
            ])
            contact_id += 1

    headers = ["contactID", "studentID", "firstname", "lastname", "relationship", "nativelanguage", "homestreet", "homestreet2", "homecity", "homestate", "homezip", "mailstreet", "mailstreet2", "mailcity", "mailstate", "mailzip", "sendmail"]

    with open(contact_file, "w") as contact_f:
        contact_f.write("\t".join(map(str, headers)) + "\n")
        for row in contact_data:
            contact_f.write("\t".join(map(str, row)) + "\n")

    print(f"Contact data written to '{contact_file}' successfully.")

if __name__ == "__main__":
    create_contacts() #uses default file names, and 1-3 contacts per student.