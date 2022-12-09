from flask import Flask
import os
from dotenv import load_dotenv
from flaskModule.systemReader import os_data, cpu_data, memory_data

# mode setup
load_dotenv()
mode = os.getenv('RESTFUL_MODE')
port = os.getenv('RESTFUL_PORT')
devPort = os.getenv('RESTFUL_DEV_PORT')
__main__ = "FORMAL"
__dev__ = "DEV"
app = Flask(mode)


@app.route("/")
def hello():
    return "It works!"


@app.route("/systemInfo")
def system_info():
    mainDict = {}
    mainDict["os"] = os_data()
    mainDict["cpu"] = cpu_data()
    mainDict["memory"] = memory_data()
    return mainDict


@app.route("/systemInfo/<mode>")
def system_info_single(mode):
    if mode == "os":
        return os_data()
    elif mode == "cpu":
        return cpu_data()
    elif mode == "memory":
        return memory_data()
    return {}

# Init


def run_app():
    global app
    if mode == __main__:
        from waitress import serve
        serve(app, port=port)
    elif mode == __dev__:
        app.run(port=devPort)


run_app()
