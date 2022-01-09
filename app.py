from flask import Flask, render_template, request, redirect, url_for
from script import predict_class

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/samples")
def samples():
    return render_template("samples.html")

@app.route("/classify", methods=['POST', 'GET'])
def classify():
    if request.method == "POST":
        print("inside the request")
        file = request.files['input_file']
        file.save("./media/image.jpeg")
        return redirect(url_for("result"))
    return render_template("classify.html")

@app.route("/result")
def result():
    prediction = predict_class("./media/image.jpeg")
    print(prediction)
    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(port=8000, debug=True)