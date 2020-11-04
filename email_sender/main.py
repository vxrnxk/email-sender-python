import smtplib


to = input("Enter the email of the recipent: ")
content = input('Enter the email content: ')

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls
    server.login('<senderemail@gmail.com>', '<password>')
    server.sendemail('<senderemail@gmail.com>', to, content)
    server.close()


sendEmail(to, content)