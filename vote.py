from datetime import datetime

def can_vote(year_born):
    current_year = datetime.now().year
    age = current_year - year_born
    if age >= 18:
        return True
    else:
        return False

# Prompt the user to enter their birth year
year_born = int(input("Enter the year you were born: "))

# Check if the user is eligible to vote
if can_vote(year_born):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
