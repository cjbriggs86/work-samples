import random
import datetime

def generate_random_data_with_errors(num_records=100, missing_data_rate=0.05, duplicate_row_rate=0.05):
    """
    Generates random student data with randomized errors (missing info, duplicate rows).

    Args:
        num_records (int): The number of base records to generate before adding duplicates.
        missing_data_rate (float): The probability (0.0 to 1.0) that a field will be missing.
        duplicate_row_rate (float): The probability (0.0 to 1.0) that a generated record will be duplicated.

    Returns:
        list: A list of lists, where each inner list is a row of student data.
    """

    first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack",
                   "Karen", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Ryan", "Sophia", "Thomas"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
                  "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
    genders = ["Male", "Female", "Other"]
    languages = ["English", "Spanish", "French", "German", "Chinese", "Japanese", "Korean", "Arabic", "Russian", "Hindi"]
    states = ["CA", "NY", "TX", "FL", "IL", "PA", "OH", "GA", "NC", "MI"]
    cities = ["Los Angeles", "New York", "Houston", "Miami", "Chicago", "Philadelphia", "Columbus", "Atlanta", "Raleigh", "Detroit"]

    base_data = []
    for i in range(num_records):
        # Generate base data for a single record
        student_id = random.randint(100000, 999999)
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        start_date = datetime.date(1995, 1, 1)
        end_date = datetime.date(2005, 12, 31)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        birthdate = (start_date + datetime.timedelta(days=random_number_of_days)).strftime("%Y-%m-%d")
        gender = random.choice(genders)
        language = random.choice(languages)
        street_num = random.randint(100, 9999)
        street = f"{street_num} {random.choice(last_names)} St"
        street2 = f"Apt {random.randint(1, 100)}" if random.random() < 0.3 else ""
        city = random.choice(cities)
        state = random.choice(states)
        zip_code = random.randint(10000, 99999)

        mail_street = street
        mail_city = city
        mail_state = state
        mail_zip = zip_code

        current_record = [
            student_id, first_name, last_name, birthdate, gender, language,
            street, street2, city, state, zip_code,
            mail_street, mail_city, mail_state, mail_zip
        ]

        # Introduce missing data
        for j in range(len(current_record)):
            if random.random() < missing_data_rate:
                current_record[j] = "" # Set field to empty string

        base_data.append(current_record)

        # Introduce duplicate rows
        if random.random() < duplicate_row_rate:
            base_data.append(current_record) # Add a duplicate of the current record

    # Shuffle the data to mix duplicates and missing values throughout the file
    random.shuffle(base_data)
    return base_data

def write_to_file(data, filename="studentdata_witherrors.txt"):
    """
    Writes the data to a tab-delimited file.

    Args:
        data (list): The list of data rows to write.
        filename (str): The name of the file to create.
    """
    headers = ["studentid", "firstname", "lastname", "birthdate", "gender", "nativelanguage",
               "homestreet", "homeline2", "homecity", "homestate", "homezip",
               "mailstreet", "mailcity", "mailstate", "mailzip"]
    with open(filename, "w") as f:
        f.write("\t".join(headers) + "\n")
        for row in data:
            # Ensure all elements are strings before joining
            f.write("\t".join(map(str, row)) + "\n")

if __name__ == "__main__":
    # Generate 500 base records with a 5% chance of missing data per field
    # and a 5% chance of duplicating a record.
    studentdata_witherrors = generate_random_data_with_errors(
        num_records=500,
        missing_data_rate=0.05,
        duplicate_row_rate=0.05
    )
    write_to_file(studentdata_witherrors, "studentdata_witherrors.txt")
    print("studentdata_witherrors generated successfully with randomized errors.")