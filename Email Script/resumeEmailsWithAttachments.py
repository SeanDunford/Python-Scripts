import os, re
import sys
import smtplib
 
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

def sendEmail(recipient, company):
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
     
    sender = 'sdunford@mail.usf.edu'
    password = "testing"
    messagePart1 = "Hi,\n\nMy name is Sean Dunford. I am a senior at the University of South Florida in Tampa, FL. I am interested in pursuing a game development internship over the summer. Does "
    messagePart2 = " have any opportunities available? Attached is a copy of my resume and cover letter. I hope to hear back from you.\n\n Thank you for your time.\n-- \nSincerely Sean Dunford,\nUniversity of South Florida\n(813) 418 - 9757\nwww.seandunford.com"

    directory = "Z:/GitProjects/Python Scripts/Email Script/attachments"
     
    sleep(30.0)

    aFile = open('results.abc', 'w')
    results = "" 
    name = ""
    email = ""

    msg = MIMEMultipart()
    msg['Subject'] = 'I totally sent this from a Python Script'
    msg['To'] = recipient
    msg['From'] = sender
     
    files = os.listdir(directory)
    pdfSearch = re.compile(".pdf", re.IGNORECASE)
    files = filter(pdfSearch.search, files)
    for filename in files:
        path = os.path.join(directory, filename)
        if not os.path.isfile(path):
            continue
     
        PDFattachment = MIMEImage(open(path, 'rb').read(), _subtype="pdf")
        PDFattachment.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(PDFattachment)
     
    part = MIMEText('text', "plain")
    message = messagePart1 + company + messagePart2
    part.set_payload(message)
    msg.attach(part)

    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, password)

    session.sendmail(sender, recipient, msg.as_string())
    session.quit()
sendEmail("jlucero2@mail.usf.edu","Growler Bears Inc.")
sendEmail("sdunford@mail.usf.edu","Software Bytes")
