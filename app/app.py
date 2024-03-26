from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def indexHandler():
    return render_template("index.html")

@app.route("/result", methods=["GET"])
def resultHandler():
    inputNum = request.args.get("userinput", type=int)
    return render_template("result.html", seed=inputNum)


#おまじない
if __name__ == "__main__":
    app.run(debug=True)
