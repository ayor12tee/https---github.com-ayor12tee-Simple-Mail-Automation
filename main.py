##################### Normal Starting Project ######################
from datetime import datetime
import pandas
import random
import smtplib

my_email = "thepeterjamil@gmail.com"
password = "hawxdrsyajjkwtgx"


# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
today = datetime.now()
print(today)
today_tuple = (today.month, today.day)
print(today_tuple)
# HINT 2: Use pandas to read the birthdays.csv file

data = pandas.read_csv("birthdays.csv")
print(data.iterrows())
#Dictionary comprehension template for pandas DataFrame looks like this:
birthdays_dict = {(data_row['month'], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
#print(birthdays_dict)


#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_person["email"],
                msg = f"Subject:Happy Birthday!\n\n{contents}"
                        )
        
            connection.quit()



