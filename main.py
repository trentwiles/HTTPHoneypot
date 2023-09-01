from flask import Flask, render_template, redirect, request
import logger
import webhook
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favi():
    return ""

def nullroute():
    return ""

@app.route('/wp-login.php', methods=["GET"])
def wplogin():
    return render_template('login.html')

@app.route('/wp-login.php', methods=["POST"])
def wploginredir():
    try:
        ua = request.headers.get('User-Agent')
    except:
        ua = ""
    dst = "443" if request.environ.get('wsgi.url_scheme') == 'https' else "80"
    #print(logger.createAbuseTemplate(request.environ['HTTP_X_FORWARDED_FOR'], request.path, request.method, ua, dst, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    x = logger.report(request.environ['HTTP_X_FORWARDED_FOR'], logger.createAbuseTemplate(request.environ['HTTP_X_FORWARDED_FOR'], request.path, request.method, ua, dst, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    return redirect('/wp-login.php')

@app.route('/<path>', methods=["GET", "POST", "DELETE", "HEAD", "OPTIONS"])
def any(path):
    try:
        ua = request.headers.get('User-Agent')
    except:
        ua = ""
    dst = "443"
    #print(logger.createAbuseTemplate(request.environ['HTTP_X_FORWARDED_FOR'], request.path, request.method, ua, dst, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    x = logger.report(request.environ['HTTP_X_FORWARDED_FOR'], logger.createAbuseTemplate(request.environ['HTTP_X_FORWARDED_FOR'], request.path, request.method, ua, dst, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    return ""


if __name__ == '__main__':
    app.run(port=18291)