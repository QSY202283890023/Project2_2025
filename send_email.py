# Program Title: send email
# Program Decription: Sample script for sending email via QQ's SMTP server
# Name: Siyuan QIn
# Student ID:202283890023
# Course&Year: Project Semester 3 & Grade 3
# Date: 20/4/2025

import smtplib  
from email.message import EmailMessage  
  
from_email_addr = "3072836362@qq.com"  
from_email_pass = "hytbvsttqribdchg"  
to_email_addr   = "2074474233@qq.com"  

  
msg = EmailMessage()  
 
body = "Hello from Raspberry Pi"  
msg.set_content(body)  
  
msg["From"] = from_email_addr  
msg["To"]   = to_email_addr  
  
msg["Subject"] = "TEST EMAIL"  
  
server = smtplib.SMTP("smtp.qq.com", 587)  

server.starttls()  
 
server.login(from_email_addr, from_email_pass)  
  
server.send_message(msg)  

print("Email sent")  
  
server.quit()  
