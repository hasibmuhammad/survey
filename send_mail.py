import smtplib
from email.mime.text import MIMEText


def send_mail(user, issue, rating, comment):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    username = '3ac0d53b84ca59'
    password = '4cf3d88d870c63'
    message = f"<h3>New Survey Submission</h3><ul><li>User: {user}</li><li>Issue: {issue}</li><li>Rating: {rating}</li><li>Comments: {comment}</li></ul>"

    sender_email = 'example@example.com'
    receiver_email = 'example2@example.com'

    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Feedback from users!'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # send the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
