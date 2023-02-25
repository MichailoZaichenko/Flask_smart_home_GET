from flask import Flask
from flask import url_for, render_template, send_file, redirect, request
import json
app = Flask(__name__)



@app.route('/')
def home(): 
    with open("example.json", "r") as file:
        data = json.load(file)
    return render_template("index.html", head1="head", title = "Smart home", temperature = data['temperature'], humidity = data["humidity"], electricity = data["meter"]["electricity"]["consumption"], gas = data["meter"]["gas"]["consumption"], water = data["meter"]["water"]["consumption"], boiler_temp = data['boiler']["temperature"], boiler_pres = data['boiler']["pressure"], IsRan = data['boiler']['isRun'])

@app.route('/api')
def any_funk(): 
    with open("example.json", "r") as file:
        data = json.load(file)
    if "temp" in request.args.keys():
        return render_template("index.html", temperature = data['temperature'] )
    elif "gas" in request.args.keys():
        return render_template("index.html", gas = data["meter"]["gas"]["consumption"] )
    elif "humidity" in request.args.keys():
        return render_template("index.html", humidity = data["humidity"] )
    elif "electricity" in request.args.keys():
        return render_template("index.html", electricity = data["meter"]["electricity"]["consumption"] )
    elif "water" in request.args.keys():
        return render_template("index.html", water = data["meter"]["water"]["consumption"] )
    elif "boiler_temp" in request.args.keys():
        return render_template("index.html", boiler_temp = data['boiler']["temperature"] )
    elif "boiler_pres" in request.args.keys():
        return render_template("index.html", boiler_pres = data['boiler']["pressure"] )
    elif "IsRan" in request.args.keys():
        return render_template("index.html", IsRan = data['boiler']['isRun'] )
    else:
        return render_template("index.html", head1="head", title = "Smart home", temperature = data['temperature'], humidity = data["humidity"], electricity = data["meter"]["electricity"]["consumption"], gas = data["meter"]["gas"]["consumption"], water = data["meter"]["water"]["consumption"], boiler_temp = data['boiler']["temperature"], boiler_pres = data['boiler']["pressure"], IsRan = data['boiler']['isRun'])


if __name__ == '__main__':
    app.run(debug=True)
