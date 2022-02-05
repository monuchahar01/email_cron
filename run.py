import smtplib, ssl
import bs4,webbrowser
import requests
import time


def sendMail():
    smtp_server = "smtp.gmail.com"
    port = 587                                    # For starttls
    sender_email = "cmonu790@gmail.com"               #sender's mail id
    receiver_email  = ['monuchahar01@gmail.com']        #list of reciever's mail ids
    #password = getpass.getpass(prompt="Type your password and press enter: ")
    password = "Ibelieveinu@7890"

    print('Runnning in a mail function\n')
    file1 = open("data.txt","r")  
    number = file1.read() 
    file1.close() 


    subject="Daily Puzzle {}".format(int(number))
    #puzzle_link=getLink(number)
    text = 'Good morning! Here\'s your puzzle for today.\n '
    message = 'Subject: {}\n\n{}'.format(subject, text)
    
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()                               # Can be omitted
        server.starttls(context=context)            # Secure the connection
        server.ehlo()                               
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        file1 = open("data.txt","w")  
        number = file1.write(str(int(number)+1)) 
        file1.close() 
        print('Runnning out from mail function\n')
    
    except Exception as e:
        print(e)

if __name__=="__main__":
    sendMail()
    
    
