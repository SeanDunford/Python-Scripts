import csv
import os, re
import sys
import smtplib

from random import randint 
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep
 
def sendEmail(recipient, company):

   SMTP_SERVER = 'smtp.gmail.com'
   SMTP_PORT = 587
    
   sender = 'sdunford@mail.usf.edu'
   password = "@@pples55"
   messagePart1 = "Hi,\n\nMy name is Sean Dunford. I am a senior at the University of South Florida in Tampa, FL. I am interested in pursuing a game development internship over the summer. Does "
   messagePart2 = " have any opportunities available? Attached is a copy of my resume and cover letter. I hope to hear back from you.\n\n Thank you for your time.\n-- \nSincerely Sean Dunford,\nUniversity of South Florida\n(813) 418 - 9757\nwww.seandunford.com"

   directory = "Z:/GitProjects/Python Scripts/Email Script/attachments" #change to Copies of resume make sure they are pdf or change extension below
   
   x = randint(9, 35)
   sleep(x)     #makes sure it's random so gMail wont mark as spam

   aFile = open('results.abc', 'w')
   results = "" 
   msg = MIMEMultipart()
   msg['Subject'] = 'Game Development Internship'
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
   print("recipient:" + recipient)
   print("company:" + company)
   print("sender:" + sender) 
   session.sendmail(sender, recipient, msg.as_string())
   session.quit()



iFile = open('Z:/GitProjects/Python Scripts/Email Script/Source sites/source.csv') #name,email .csv
reader = csv.reader(iFile)


aFile = open('results.abc', 'w')#prints results
results = "" 
name = ""
email = ""
rownum = 0
emailCount = 0
for row in reader: 
   #save header row
   if rownum == 0:
      header = row
   else:
      colnum = 0
      for col in row:
        if colnum == 0:
           name = col
        else:
           email = col
        results += col
        colnum = colnum + 1
   #print (name + ' ' + email)
   if((email != "") & (name != "") & (emailCount <=20000)):
     sendEmail(email, name)
     emailCount += 1
     print("sending email to " + name + " at " + email + "....."+ str(emailCount))
   aFile.write(results + '\n')
   results = ''
   rownum += 1
aFile.close()