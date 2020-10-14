from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("info_index.html")


if __name__ == "__main__":
    app.run(port=8000)