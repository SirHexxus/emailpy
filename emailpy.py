import smtplib
import ssl
import os
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

SENDER = os.getenv('SENDER')
PASS = os.getenv('PASS')


def main():
    subject = 'Test email from Python'
    body = 'This is a test email from Python.'
    sender_email = SENDER
    receiver_email = input('Enter receiver email: ')
    password = PASS

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
        </body>
    </html>
    """

    message.add_alternative(html, subtype="html")

    context = ssl.create_default_context()

    print("Sending Email...")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent!")


if __name__ == "__main__":
    main()
