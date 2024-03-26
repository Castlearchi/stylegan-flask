from flask import Flask, render_template, request, send_from_directory
from app.run_stylegan import run_stylegan
import os

IMGDIR = "static/"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = IMGDIR

@app.route("/")
def handleIndex():
    return render_template("index.html")


@app.route("/result", methods=["GET"])
def handleResult():
    inputNum = request.args.get("userinput", type=int)
    imgpath = os.path.join(app.config["UPLOAD_FOLDER"], "result.png")
    run_stylegan(inputNum, imgpath)
    return render_template("result.html", seed=inputNum, image=imgpath)


if __name__ == "__main__":
    app.run(debug=True)
