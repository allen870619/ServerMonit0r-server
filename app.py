from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()
mode = os.getenv('RESTFUL_MODE')
port = os.getenv('RESTFUL_PORT')
__main__ = "FORMAL"
__dev__ = "DEV"
app = Flask(mode)

@app.route("/")
def test():
    return "It works!"

# Init
def runApp():
    global app
    if mode == __main__:
        from waitress import serve
        serve(app, port=port)
    elif mode == __dev__:
        app.run(port=8787)
runApp()