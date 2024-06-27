import smtplib, ssl
import streamlit as st

def sendemail(message):
    host = "smtp.gmail.com"
    port = 465

    username = st.secrets[SE_USERNAME]
    password = st.secrets[SE_PASSWORD]

    receiver = st.secrets[SE_USERNAME]
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port, context = context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
