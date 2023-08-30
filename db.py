import os

def write(ip):
    with open('db.txt', 'a') as w:
        w.write(ip + "\n")

def search(ip):
    with open('db.txt', 'r') as w:
        for x in w.readlines():
            if ip == x:
                return True
    return False

def clear():
    if os.path.exists('db.txt'):
        os.remove('db.txt')