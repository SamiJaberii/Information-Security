import smtplib
from email.mime.text import MIMEText

sender = "js12245@auca.kg"
password = "difc rjgb uzuw omva"

receiver = "js12245@auca.kg"

msg = MIMEText("Open this link: file:///Users/samijabery/Desktop/Information-Security/Lab-4/phishing/index.html")

msg["Subject"] = "Verification required"
msg["From"] = sender
msg["To"] = receiver

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)

server.sendmail(sender, receiver, msg.as_string())

server.quit()
