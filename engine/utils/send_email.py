from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from .email_constants import message_text, message



def send_email(receiver, content):
    message = MIMEMultipart()
    sender = 'support@zimtickets.com'
    title = "Thank you."
    password="@MviyoLaunch2023"
    email_host = "smtp-mail.outlook.com"
    email_port = "587"
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = title
    message.attach(MIMEText(content, "html"))
    session = smtplib.SMTP(email_host, email_port)
    session.starttls()
    session.login(sender, password)
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()


message_ = message()
message_info = message_text(message_, f"Good Day")
send_email("tyronemguni@gmail.com", message_info)