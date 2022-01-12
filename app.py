from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "see my own website made by chethan"
