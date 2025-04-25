class Profile:
    def __init__(self, name, email, class_year, gender, field_of_study, interests, filters):
        self.name = name
        self.email = email
        self.class_year = class_year
        self.field_of_study = field_of_study
        self.interests = interests  # dict of lists
        self.filters = filters      # dict of strings

    def __repr__(self):
        return f"UserProfile({self.name}, {self.email})"

def email_validate(database):
    while True:
        email = input("Enter your email: ")
        print(database)
        if email in database: 
            print("Email already in database. Please use another email.")
        else:        
            if "@" in email and "." in email:
                return email
            print("Invalid email format. Please try again.")

def class_year_validate(any_bool):
    valid_years = ["2025", "2026", "2027", "2028"]
    if any_bool:
        valid_years.append("any")
    while True:
        if not any_bool:
            input_msg = "Enter your class year (2025–2028): "
        else: 
            input_msg = "Preferred class year (2025-2028 or 'any' if no preference): "
        class_year = input(input_msg).lower()
        if class_year in valid_years:
            return class_year
        print("Invalid class year. Must be one of 2025, 2026, 2027, or 2028.")

def gender_validate(any_bool):
    valid_genders = ["male", "female", "nonbinary", "other"]
    if any_bool:
        valid_genders.append("any")
    while True:
        if not any_bool:
            input_msg= "Enter your gender ('male', 'female', 'nonbinary', or 'other'): "
        else:
            input_msg="Preferred gender ('male', 'female', 'nonbinary', 'other', or 'any' if no preference): "
        gender = input(input_msg).lower()
        if gender in valid_genders:
            return gender
        print("Invalid gender. Must be one of male, female, nonbinary, or other.")

def field_of_study_validate(any_bool):
    valid_fields = ["arts","engineering","history","languages and literature", "life sciences", "math and computation", "physical sciences", "qualitative social sciences", "quantitative social sciences"]
    if any_bool:
        valid_fields.append("any")

    while True:
        if not any_bool:
            input_msg = 'Select your field of study from the list below:\nArts / Engineering / History / Languages and Literature / Life Sciences / Math and Computation / Physical Sciences / Qualitative Social Sciences / Quantities Social Sciences\n'
        else:
            input_msg = "Select your preferred field of study from the list below:\nArts / Engineering / History / Languages and Literature / Life Sciences / Math and Computation / Physical Sciences / Qualitative Social Sciences / Quantities Social Sciences\n\nEnter 'any' if no preference\n"
        field_of_study = input(input_msg).lower()
        if field_of_study in valid_fields:
            return field_of_study
        print("Invalid field of study. Must be one of the above list.")

def create_profile(database):
    name = input("Enter your name: ")
    email = email_validate(database)
    class_year = class_year_validate(False)
    gender = gender_validate(False)
    field_of_study = field_of_study_validate(False)

    academic = input("Academic interests (comma-separated): ").split(",")
    career = input("Career interests (comma-separated): ").split(",")
    extracurricular = input("Extracurricular interests (comma-separated): ").split(",")

    interests = {
        "academic": [i.strip().lower() for i in academic],
        "career": [i.strip().lower() for i in career],
        "extracurricular": [i.strip().lower() for i in extracurricular],
    }

    filters = {
        "gender": gender_validate(True),
        "field_of_study": field_of_study_validate(True),
        "class_year": class_year_validate(True),
    }

    return Profile(name, email, class_year, gender, field_of_study, interests, filters)

def main():
    print("Welcome to our platform! Please create your profile.")

    # this is placeholder database - need a global variable to store users
    userdatabase = []
    user = create_profile(userdatabase)  # Create the profile by prompting the user

    print(f"\nThanks, {user.name}! Your profile has been created:")
    print(user)  # Uses __repr__ to show name and email

    # Example: access a specific field
    print(f"\nYou're interested in:")
    for category, items in user.interests.items():
        print(f"  {category.title()}: {', '.join(items)}")

    # You can also store multiple users:
    userdatabase.append(user)

    # Later in your program, this list can be used for filtering/matching
    # For example:
    # match_candidates = [other for other in all_users if some_match_logic(user, other)]

if __name__ == "__main__":
    main()
