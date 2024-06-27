import streamlit as sl
from sendemail import sendemail

sl.header("Contact Me")

with sl.form(key="email"):
    useremail = sl.text_input("Your Email Address")
    message = sl.text_area("Your message:")
    messagefl = f"""\
Subject: Portfolio Project {useremail}

From: {useremail}
{message}
"""
    button = sl.form_submit_button(label="Submit")
    if button:
        sendemail(messagefl)
        sl.info("Your email was sent successfully.")
