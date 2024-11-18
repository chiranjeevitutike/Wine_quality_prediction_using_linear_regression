import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

model = pickle.load(open("wine.pkl", "rb"))

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET"])
def predict():
    ip_cols = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    l1 = []
    for i in ip_cols:
        va = request.args.get(i)
        if va is not None:
            l1.append(float(va))
    pr = model.predict([l1])
    return str(list(pr))

if __name__ == '__main__':
    app.run(debug=True)
