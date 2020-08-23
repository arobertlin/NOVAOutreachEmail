import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

first_names = []
emails = []
with open('names.csv', encoding="utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        names = row[0]
        first_name = names.split()[0]
        first_names.append(first_name)

        email = row[1]
        emails.append(email)

if len(first_names) != len(emails):
    raise ValueError(
        'Mismatching lengths of names to emails. Check to see that lists are equal sizes and matched up correctly')

password = input("Type your password and press enter:")

for i in range(len(first_names)):
    print(first_names[i], emails[i])

    sender_email = "email" # FILL THIS IN
    receiver_email = emails[i]

    message = MIMEMultipart("alternative")
    message["Subject"] = "Christian Union NOVA"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """Hi """+ first_names[i] + """!
    Welcome to Princeton! I’m NAME, a senior and a member of a Christian group on campus called Christian Union NOVA, and each year we like to reach out to the incoming class early on to invite you to become part of our large, supportive community. Trust me, it’s a great community to be a part of! NOVA is filled with really likable, awesome people from all four classes, which makes you feel like you have tons of friends and endless sources of guidance.
    
    On a more intimate level, NOVA offers bible studies that meet once a week. There are also large weekly meetings called Encounter and Tru Thursday, as well as one-on-one parternships with older students. I know remote learning will make it even more challenging to start a new school and make friends, so hopefully NOVA's community can help you start making sense of Princeton! If you're interested in learning more, the NOVA open house zoom link is https://princeton.zoom.us/j/92218456650 and is coming up soon on Thursday, August 27th from 8-9 ET.
    
    You can also follow our accounts on Instagram if you would like to learn more (@christianunionnova) and (@TruThursday). There may be a gear giveaway on them so be on the lookout!
    
    Can’t wait to meet you! Good luck with everything!
    NAME
    """
    html = """\
    <html>
      <body>
        <p>
        Hi """ + first_names[i] + """! <br><br>
        Welcome to Princeton! I’m NAME, a senior and a member of a Christian group on campus called Christian Union NOVA,
        and each year we like to reach out to the incoming class early on to invite you to become part of our large, supportive community.
        Trust me, it’s a great community to be a part of! NOVA is filled with really likable, awesome people from all four classes,
        which makes you feel like you have tons of friends and endless sources of guidance.<br><br>
    
        On a more intimate level, NOVA offers bible studies that meet once a week. There are also large weekly meetings called
        Encounter and Tru Thursday, as well as one-on-one parternships with older students. I know remote learning will make it
        even more challenging to start a new school and make friends, so hopefully NOVA's community can help you start making sense of
        Princeton! If you're interested in learning more, the NOVA open house can be found at
           <a href="https://princeton.zoom.us/j/92218456650
        ">this</a>
        zoom link, and is coming up soon on Thursday, August 27th from 8-9 ET. <br><br>
    
        You can also follow our accounts on Instagram if you would like to learn more (@christianunionnova) and (@TruThursday).
    There may be a gear giveaway on them so be on the lookout!
    <br><br>
        Can’t wait to meet you! Good luck with everything!<br>
        NAME</p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
