##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import smtplib
import random
my_email="meghnaperuri222@gmail.com"
password="awjqsxdrmduedxus"

# 1. Update the birthdays.csv
df=pd.read_csv("birthdays.csv")
print(df)

# 2. Check if today matches a birthday in the birthdays.csv
now=dt.datetime.now()
year=now.year
day=now.day
month=now.month
name=""

for index,row in df.iterrows():
    # print("hello")
    name=row["name"]
    email=row["email"]
    if row["year"]==year and row["month"]==month and row["day"]==day:

        letters_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        random_letter = random.choice(letters_list)
        print(random_letter)
        # random_letter="letter_1.txt"

        with open(f"./letter_templates/{random_letter}", "r") as f:
            lines = f.readlines()
        # print(lines)
        modified_lines = [line.replace("[name]", name) for line in lines]
        print(modified_lines)

        with open(f"./letter_templates/{random_letter}", "w") as f:
            for line in modified_lines:
                f.write(line)
        with open(f"./letter_templates/{random_letter}","r") as f:
            file_content=f.read()

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"subject: birthday wishes\n\n{file_content}"
            )

print(name)#using python anywhere



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

