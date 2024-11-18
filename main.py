import pickle 
from flask import Flask,request

app=Flask(__name__)

model=pickle.load(open("wine.pkl","rb"))

@app.route("/predict",methods=["GET"])
def predict():
    ip_cols=["a","b","c","d","e","f","g","h","i","j","k"]
    l1=[]
    for i in ip_cols:
        va=request.args.get(i)
        l1.append(eval(va))
    pr=model.predict([l1])
    return str(list(pr))


if __name__=='__main__':
    app.run(debug=True)
