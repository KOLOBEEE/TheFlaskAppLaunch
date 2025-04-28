from flask import Flask, render_template, redirect, session, url_for


app = Flask(__name__)

@app.route("/")
def home():
    return "Kolobe, you are doing great!"






if __name__ == "__main__":
    app.run(debug=True)