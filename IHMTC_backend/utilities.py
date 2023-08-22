import getpass
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

HOST = "smtp-mail.outlook.com"
PORT = 587

def send_reset_link(email, token):
    FROM_EMAIL = "tejas_2101cs78@iitp.ac.in"
    TO_EMAIL = email
    PASSWORD = os.getenv("PASSWORD")

    MESSAGE = f"""Subject: IHMTC Reset Password

    Dear User,

    To reset your password, please follow this link: http://localhost:8000/reset-password/{token}

    If you didn't initiate this request or if you have any concerns, please feel free to contact our support team at [support@email.com] or call us at [support phone number].

    Thank you for being a valued member of our community.

    Best regards,
    IHMTC IIT Patna"""

    smtp = smtplib.SMTP(HOST, PORT)
    status_code, response = smtp.ehlo()
    print(f"Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"Starting TLS Connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"Logging in: {status_code} {response}")

    smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
    smtp.quit()
