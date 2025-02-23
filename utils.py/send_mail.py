# https://realpython.com/python-send-email/

import smtplib
from os import getenv
from sys import exit
from ssl import create_default_context


SENDER = "admin@test.com"  # replace with correct domain for test


port = getenv("SMTP_PORT")
if port == '' or None:
    port = 465

password = getenv("SMTP_PASSWORD")
if password == '' or None:
    exit("No SMTP password found in Env.", 1)

smtp_user = getenv("SMTP_USER")
if smtp_user == '' or None:
    exit("No SMTP user found in Env.", 2)

smtp_server = getenv("SMTP_SERVER")
if smtp_server == '' or None:
    exit("No SMTP Server found in Env", 3)


ssl_context = create_default_context()


def send_message(reciver: str, message: str) -> None:
    with smtplib.SMTP_SSL(smtp_server, port, context=ssl_context) as server:
        server.login(user=smtp_user, password=password)
        server.sendmail(SENDER, reciver, message)
