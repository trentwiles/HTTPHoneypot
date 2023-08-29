from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/favicon.ico')

def nullroute():
    return ""

@app.route('/wp-login.php', methods=["POST", "GET"])
def wplogin():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)