import requests
import json
from querycontacts import ContactFinder
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

qf = ContactFinder()

def email(subject, to, data):
    sg = sendgrid.SendGridAPIClient(api_key=json.loads(open('config.json').read())['key'])
    from_email = Email(json.loads(open('config.json').read())['from'])
    to_email = To(to)
    content = Content("text/plain", data)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.headers)
    return


def report(ip, path):
    abuse = qf.find(ip)
    if len(abuse) == 0:
        return None
    for x in abuse:
        print()
    return ""