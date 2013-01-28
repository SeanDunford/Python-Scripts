import smtplib
import string



SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587

sender = 'sdunford@mail.usf.edu'
recipient = 'jlucero2@mail.usf.edu'
subject = 'Gmail SMTP Test'
body = 'blah blah blah'

"Sends an email to the specified recipient"

body = "" + body + ""

headers = ["from: " + sender,
           "subject: " + subject,
           "to: " + recipient,
           "mime-version: 1.0",
           "content-type: text/html"]
headers = "\r\n".join(headers)

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

session.ehlo()
session.starttls()
session.ehlo
session.login('sdunford@mail.usf.edu', 'password')
session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
session.quit()