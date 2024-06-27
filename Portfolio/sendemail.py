import smtplib, ssl

def sendemail(message):
    host = "smtp.gmail.com"
    port = 465

    username = USERNAME
    password = PASSWORD

    receiver = "madheshwaran63@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port, context = context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
