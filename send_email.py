# Import Libraries
import random
import smtplib
import ssl
from email.message import EmailMessage

# All receivers' emails (Change it to your receivers' email address)
receivers_email = {
    "Eunha": "fake1@gmail.com",
    "Sowon": "fake2@gmail.com",
    "Yerin": "fake3@gmail.com",
}

# Shuffle the receivers
name = ["Eunha", "Sowon", "Yerin"]
random.shuffle(name)


# After shuffling the order of names, pair individuals in the sequence.
match_dict = {}

for i, sender in enumerate(name):
    if i != len(name) - 1:
        receiver = name[i + 1]
    else:
        receiver = name[0]
    match_dict[sender] = receiver

# Send Email
for sender, receiver in match_dict.items():
    subject = "Christmas Gift Exchange Draw"
    body = "Your gift exchange partner is: " + receiver
    sender_email = "fake_sender@gmail.com"
    receiver_email = receivers_email[sender]
    password = "wodj bpwb kael qmog"

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
        </body>
    </html>
    """

    message.add_alternative(html, subtype="html")
    context = ssl.create_default_context()

    print("Sending Email")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Successfully sent email")
