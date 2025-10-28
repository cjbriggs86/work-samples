import random
import datetime

def generate_random_admins(num_records=50):

    """
    AdminID (unique ID)
    First Name
    Last Name
    Service Type
    Credential
    Valid Start Date
    Valid End Date   
    Show
    """

    types_first_names = ["Alice", "Bryan", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack", "Doctor",
                   "Karen", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Ryan", "Sophia", "Thomas", "Zedd", "Tiesto"]
    types_last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
                  "Hernandez", "Lopez", "Gonzalez", "Briggs", "Meyer", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
    types_services = ["Physical Therapist", "Speech Therapist", "Occupational Therapist", "Audiologist", "Interpreter",
                     "Recreactional Therapist", "Mobility Therapist", "School Nurse", "Social Worker", "Guidance Counselor"]
    # keeps track of the corresponding values, manually assigned within loop
    # credential_types = ["PT", "ST", "OT", "AU", "I", "RT", "MT", "RN", "SW", "GC"]

    types_show = ["Yes", "No"]
    
    data = []
    for i in range(num_records):
        adminID = 1000 + i
        first_name = random.choice(types_first_names)
        last_name = random.choice(types_last_names)
        service_type = random.choice(types_services)
        
        # selects the appropriate credential to match the randomly selected service type
        if service_type == "Physical Therapist": credential_type = "PT"
        if service_type == "Speech Therapist": credential_type = "ST"
        if service_type == "Occupational Therapist": credential_type = "OT"
        if service_type == "Audiologist": credential_type = "AU"
        if service_type == "Interpreter": credential_type = "I"
        if service_type == "Recreactional Therapist": credential_type = "RT"
        if service_type == "Mobility Therapist": credential_type = "MT"
        if service_type == "School Nurse": credential_type = "RN"
        if service_type == "Social Worker": credential_type = "SW"
        if service_type == "Guidance Counselor": credential_type = "GC"
        
        # randomizes credential start date, then adds end date 2 years after that
        start_date = datetime.date(1995, 1, 1)
        end_date = datetime.date(2005, 12, 31)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        valid_start = start_date + datetime.timedelta(days = random_number_of_days)
        valid_end = valid_start + datetime.timedelta(days = 730)

        show_setting = "Yes"
        # show_setting = random.choice(types_show)

        data.append([adminID, first_name, last_name, service_type, credential_type, valid_start.strftime("%Y-%m-%d"), valid_end.strftime("%Y-%m-%d"), show_setting])

    return data

def write_to_file(data, filename="administrators.txt"):
    # writes the data to a tab-delimited file
    headers = ["adminID", "firstname", "lastname", "service_type", "credential", "cred_start", "cred_end", "show"]
    with open(filename, "w") as f:
        f.write("\t".join(headers) + "\n")
        for row in data:
            f.write("\t".join(map(str, row)) + "\n")

if __name__ == "__main__":
    admin_data = generate_random_admins(50) #Generate 50 records.
    write_to_file(admin_data)
    print("administrators.txt generated successfully.")