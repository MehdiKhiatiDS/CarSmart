from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Carsmart aws landing page!"

if __name__ ==  '__main__':
    app.run()
