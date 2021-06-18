import os
import smtplib
if os.path.exists("env.py"):
    import env


# smtp send email function
def send_email(to_list, subject, message):
    email_login = os.environ.get("EMAIL_LOGIN")
    email_pass = os.environ.get("EMAIL_PASS")

    email_text = """From: %s\r\nTo: %s\r\nSubject: %s\r\n

    %s
    """ % (email_login, ", ".join(to_list), subject, message)

    email = smtplib.SMTP("smtp.gmail.com", 587)
    email.ehlo()
    email.starttls()
    email.login(email_login, email_pass)
    email.sendmail(email_login, to_list, email_text)
    email.close()
