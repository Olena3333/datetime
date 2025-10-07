#Написати код, який буде рахувати вік людини
from datetime import datetime
#2000-01-01
def calculate_person_age(date_of_birth_str: str) -> int:
    date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d") #str parse time
    today = datetime.today()
    date_of_birth_this_year = date_of_birth.replace(year = today.year)
    print(date_of_birth_this_year)
    age = today.year - date_of_birth.year
    print(age)
    if (date_of_birth_this_year > today):
        age -= 1

    return age

calculate_person_age("2000-01-01") #25
calculate_person_age("2025-10-10") #25

def get_days_from_today(date_str: str)-> int:
    date = datetime.strptime(date_str, "%Y-%m-%d") #str parse time
    today = datetime.today()
    resalt=2
    return resalt
get_days_from_today('2020-10-09')