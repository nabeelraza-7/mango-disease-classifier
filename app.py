from flask import Flask, render_template, request
from script import predict_class

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/classify", methods=['POST', 'GET'])
def classify():
    if request.method == "POST":
        print("inside the request")
        file = request.files['image_file']
        file.save("./media/image.jpeg")
        prediction = predict_class("./media/image.jpeg")
        print(prediction)
    return render_template("classify.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)