import smtplib
import datetime as dt
import random

my_email= "thepeterjamil@gmail.com"
password = "hawxdrsyajjkwtgx"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt") as quote_files:
        all_quotes = quote_files.readlines()
        quote = random.choice(all_quotes)
        print(quote)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="oluwaseyiogunrinola@gmail.com",
                msg = f"Subject: Monday Motivation\n\n{quote}"
                        )
        
            connection.quit()
