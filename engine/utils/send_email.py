from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .email_constants import message_text
from email.mime.base import MIMEBase
from email import encoders
from decouple import config
import smtplib



def send_email(receiver, content, attachment=None):
    message = MIMEMultipart()
    sender = config('EMAIL_USERNAME')
    title = "Notification"
    username = config('EMAIL_USERNAME')
    password = config('EMAIL_PASSWORD')
    content = content
    email_host = config('EMAIL_HOST')
    email_port = config('EMAIL_PORT')
    message["From"] = sender
    message["To"] = str(receiver)
    message["Subject"] = title
    message.attach(MIMEText(message_text(content, title), "html"))

    print(f"\n\n{username}, {password}\n\n")

    if attachment is not None:
        with open(attachment, 'rb') as file:
            filename, file_extension = (file.name).split(".")
            if "/" in filename:
                filename = filename.split("/")[-1]
            payload = MIMEBase("application", f"{file_extension}", Name=filename)
            payload.set_payload(file.read())
            encoders.encode_base64(payload)
            payload.add_header("Content-Disposition", "attachment", filename=filename)
            message.attach(payload)


    session = smtplib.SMTP_SSL(email_host, email_port)
    session.login(username, password)
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()