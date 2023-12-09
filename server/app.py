#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>";

@app.route("/print/<parameter>")
def print_string(parameter):
    print(parameter);
    return parameter;

@app.route("/count/<int:parameter>")
def count(parameter):
    #if (type(parameter) == int and (0 == parameter or 0 < parameter)): pass;
    #else: raise Exception("parameter must be a number!");
    mystr = "";
    for c in range(parameter):
        mystr += str(c) + "\n";
        print(c);
    return mystr;

@app.route("/math/<int:parama>/<operation>/<int:paramb>")
def math(parama, operation, paramb):
    #print(f"parama = {parama}");
    #print(f"operation = {operation}");
    #print(f"paramb = {paramb}");
    res = 0;
    if (operation == "*"): res = parama * paramb;
    elif (operation == "div"): res = parama / paramb;
    elif (operation == "+"): res = parama + paramb;
    elif (operation == "-"): res = parama - paramb;
    elif (operation == "%"): res = parama % paramb;
    elif (operation == "^"): res = math.pow(parama, paramb);
    else: raise Exception("invalid operation!");
    #print(f"res = {res}");
    return str(res);

if __name__ == '__main__':
    app.run(port=5555, debug=True)
