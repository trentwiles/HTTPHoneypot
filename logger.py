import requests
import json
from querycontacts import ContactFinder
import sendgrid
import os
import db
from sendgrid.helpers.mail import Mail, Email, To, Content

qf = ContactFinder()

def createAbuseTemplate(ip, path, http_type, ua, dst, timestamp):
    return "Hello,\n\nOur systems have detected malicous traffic from an IP address belonging to your network to a honeypot. Logs of this incident are as follows:\n\n\nIP address: " + ip + "\nHTTP request type: " + http_type + "\nHTTP request path: " + path + "\nHTTP User Agent: " + ua + "\nDestination port: " + dst + "\nTimestamp: " + timestamp + "\n\nPlease review this request and terminate the source of this threat if required.\n\nThank you,\nTrent Wiles Abuse Reporting Project"

def email(subject, to, data):
    sg = sendgrid.SendGridAPIClient(api_key=json.loads(open('config.json').read())['key'])
    from_email = Email(json.loads(open('config.json').read())['from'])
    to_email = To(to)
    content = Content("text/plain", data)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.headers)


def report(ip, createAbuseTemplateFunctionResult):
    if db.search(ip) == False:
        abuse = qf.find(ip)
        if len(abuse) == 0:
            # If there are no abuse contacts, add IP to database and move on
            db.write(ip)
            return None
        for x in abuse:
            email('Abuse Report for IP Address ' + ip, x, createAbuseTemplateFunctionResult)
        db.write(ip)