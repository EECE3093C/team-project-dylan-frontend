from flask import request, Flask
import webbrowser

app = Flask(__name__)

@app.route('/addHours', methods=['POST'])
def addHours():
    

    return (request.form['hours'])
