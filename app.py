from flask import Flask
from flask import url_for, render_template, send_file, redirect, request
import json
app = Flask(__name__)



@app.route('/')
def home(): 
    with open("example.json", "r") as file:
        data = json.load(file)
    return render_template("index.html", head1="head", title = "Smart home", temperature = data['temperature'], humidity = data["humidity"], electricity = data["meter"]["electricity"]["consumption"], gas = data["meter"]["gas"]["consumption"], water = data["meter"]["water"]["consumption"], boiler_temp = data['boiler']["temperature"], boiler_pres = data['boiler']["pressure"], IsRun = data['boiler']['isRun'])



@app.route('/api')
def any_funk(): 
    with open("example.json", "r") as file:
        data = json.load(file)
    temperature = data['temperature']
    gas = data["meter"]["gas"]["consumption"]
    humidity = data["humidity"]
    electricity = data["meter"]["electricity"]["consumption"]
    water = data["meter"]["water"]["consumption"]
    boiler_tempure = data['boiler']["temperature"]
    boiler_presure = data['boiler']["pressure"]
    IsRan = data['boiler']['isRun']
    if "temp" in request.args.keys():
        return render_template("index.html", temperature = temperature )
    elif "gas" in request.args.keys():
        return render_template("index.html", gas = gas )
    elif "humidity" in request.args.keys():
        return render_template("index.html", humidity = humidity )
    elif "electricity" in request.args.keys():
        return render_template("index.html", electricity = electricity )
    elif "water" in request.args.keys():
        return render_template("index.html", water = water )
    elif "boiler_tempure" in request.args.keys():
        return render_template("index.html", boiler_tempure = boiler_tempure )
    elif "boiler_presure" in request.args.keys():
        return render_template("index.html", boiler_presure = boiler_presure )
    elif "IsRan" in request.args.keys():
        return render_template("index.html", IsRan = IsRan )
    else:
        return render_template("index.html", head1="head", title = "Smart home", temperature = data['temperature'], humidity = data["humidity"], electricity = data["meter"]["electricity"]["consumption"], gas = data["meter"]["gas"]["consumption"], water = data["meter"]["water"]["consumption"], boiler_temp = data['boiler']["temperature"], boiler_pres = data['boiler']["pressure"], IsRun = data['boiler']['isRun'])


if __name__ == '__main__':
    app.run(debug=True)
