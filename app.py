from flask import Flask
from flask import url_for, render_template, send_file, redirect, request
from urllib.parse import urlparse, parse_qs, parse_qsl
import json
app = Flask(__name__)



@app.route('/')
def home(): 
    with open("example.json", "r") as file:
        data = json.load(file)
    return render_template("index.html", head1="head", title = "Smart home", temperature = data['temperature'], humidity = data["humidity"], electricity = data["meter"]["electricity"]["consumption"], gas = data["meter"]["gas"]["consumption"], water = data["meter"]["water"]["consumption"], boiler_tempure = data['boiler']["temperature"], boiler_presure = data['boiler']["pressure"], IsRan = data['boiler']['isRun'])

@app.route('/api')
def any_funk(): 
    with open("example.json", "r") as file:
        data = json.load(file)
        data = {
    "temperature" : 25.2,
    "humidity" : 73.6,
    "electricity" : 1.2,
    "gas" : 0.5,
    "water" : 0.1,
    "IsRan" : True,
    "boiler_tempure" : 28.2,
    "boiler_presure" : 1.6
    }
    # if "temperature" in request.args.keys():
    #     return render_template("index.html", temperature = data['temperature'] )
    # if "gas" in request.args.keys():
    #     return render_template("index.html", gas = data["meter"]["gas"]["consumption"] )
    # if "humidity" in request.args.keys():
    #     return render_template("index.html", humidity = data["humidity"] )
    # if "electricity" in request.args.keys():
    #     return render_template("index.html", electricity = data["meter"]["electricity"]["consumption"] )
    # if "water" in request.args.keys():
    #     return render_template("index.html", water = data["meter"]["water"]["consumption"] )
    # if "boiler_tempure" in request.args.keys():
    #     return render_template("index.html", boiler_tempure = data['boiler']["temperature"] )
    # if "boiler_presure" in request.args.keys():
    #     return render_template("index.html", boiler_presure = data['boiler']["pressure"] )
    # if "IsRan" in request.args.keys():
    #     return render_template("index.html", IsRan = data['boiler']['isRun'] )
    if "temperature" or "gas" or "humidity" or "electricity" or "water" or "boiler_tempure" or "boiler_presure" or "IsRan" in request.args.keys():
        return render_template("index.html", args = request.args)
    return render_template("index.html", head1="head", title = "Smart home", args = data)
    # if "temp" in request.args.keys():
    #     return render_template("index.html", temperature = data['temperature'] )
    # elif "gas" in request.args.keys():
    #     return render_template("index.html", gas = data["meter"]["gas"]["consumption"] )
    # elif "humidity" in request.args.keys():
    #     return render_template("index.html", humidity = data["humidity"] )
    # elif "electricity" in request.args.keys():
    #     return render_template("index.html", electricity = data["meter"]["electricity"]["consumption"] )
    # elif "water" in request.args.keys():
    #     return render_template("index.html", water = data["meter"]["water"]["consumption"] )
    # elif "boiler_tempure" in request.args.keys():
    #     return render_template("index.html", boiler_tempure = data['boiler']["temperature"] )
    # elif "boiler_presure" in request.args.keys():
    #     return render_template("index.html", boiler_presure = data['boiler']["pressure"] )
    # elif "IsRan" in request.args.keys():
    #     return render_template("index.html", IsRan = data['boiler']['isRun'] )
    # else:
    #     return render_template("index.html", head1="head", title = "Smart home", temperature = data['temperature'], humidity = data["humidity"], electricity = data["meter"]["electricity"]["consumption"], gas = data["meter"]["gas"]["consumption"], water = data["meter"]["water"]["consumption"], boiler_tempure = data['boiler']["temperature"], boiler_presure = data['boiler']["pressure"], IsRan = data['boiler']['isRun'])


if __name__ == '__main__':
    app.run(debug=True)
