import os

def write(ip):
    with open('db.txt', 'a') as w:
        w.write(ip + "\n")

def search(ip):
    if os.path.exists('db.txt'):
        with open('db.txt', 'a') as w:
            w.write('127.0.0.1\n')

    with open('db.txt', 'r') as w:
        for x in w.readlines():
            if ip == x:
                return True
    return False

def clear():
    if os.path.exists('db.txt'):
        os.remove('db.txt')