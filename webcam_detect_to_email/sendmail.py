import smtplib
import imghdr
from email.message import EmailMessage

username = "madheshwaran63@gmail.com"
password = "cijczluwekalanrx"
receiver = "madheshwaran63@gmail.com"

def send_email(image_path):

    email_message = EmailMessage()
    email_message["Subject"] = "Something detected by camera"
    email_message.set_content("Hey, a new intruder just popped up on your camera. Check this....")

    with open(image_path,"rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content) )
    
    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username,password)
    gmail.sendmail(username,receiver, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/image19.png")