import requests
from querycontacts import ContactFinder


qf = ContactFinder()

def report(ip, path):
    abuse = qf.find(ip)
    if len(abuse) == 0:
        return None
    return