from flask import Flask
from flask import url_for, render_template, send_file, redirect
import json
app = Flask(__name__)



@app.route('/')
def home(): 
    with open("example.json", "r") as file:
        data = json.load(file)
    return render_template("index.html", head1="head", title = "Smart home", temperature = data['temperature'], humidity = data["humidity"], electricity = data["meter"]["electricity"]["consumption"], gas = data["meter"]["gas"]["consumption"], water = data["meter"]["water"]["consumption"], boiler_temp = data['boiler']["temperature"], boiler_pres = data['boiler']["pressure"], IsRun = data['boiler']['isRun'])

if __name__ == '__main__':
    app.run(debug=True)
