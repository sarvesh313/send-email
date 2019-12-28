import smtplib

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

smtp.login(input("Enter your gmail: "), input("Enter your password: "))

subject = input("Enter a subject: ")
body = input("Enter the body of the email: ")
msg = f'Subject: {subject}\n\n{body}'

smtp.sendmail(input("Enter your gmail address: "), input("Enter the email address it is going to: "), msg)
