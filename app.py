from flask import Flask, render_template, request, session, redirect, url_for, make_response, jsonify, Response, send_file 
import pandas as pd
import statistics
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt, mpld3
from mpld3 import plugins
import matplotlib
matplotlib.use("Agg")
import io
from io import BytesIO
import json



df = pd.read_csv(r'templates\sales.csv')

app = Flask(__name__)

@app.route("/", methods=("POST", "GET"))
   
# read data from csv
def html_table():
    return render_template('index.html',  tables=[df.to_html(classes='data', index=False)], titles=df.columns.values)

#total sales   
@app.route("/sales", methods=("POST", "GET"))
def sales_total():
    total = sum(df["sales"])
    s = "Total sales are {} GBP".format(total)
    return jsonify(result =s)

# Minimum sale
@app.route("/minimum", methods=("POST", "GET"))
def minim():
    month_sales = df[["month", "sales"]]
    arr = month_sales.to_records()
    minimum = min (arr, key=lambda  month: month[-1])
    m = "The month with min sales is {}".format(minimum)
    return jsonify(result=m)

# Maximum sale
@app.route("/maximum", methods=("POST", "GET"))
def maxim():
    month_sales = df[["month", "sales"]]
    arr = month_sales.to_records()
    maximum = max(arr, key=lambda  month: month[-1])
    x = "The month with max sales is {}".format(maximum)
    return jsonify(result=x)

# Average

@app.route("/average", methods=("POST", "GET"))
def average():
    avge = statistics.mean(df["sales"])
    a="Average is {}".format(round(avge))
    return jsonify (result =a)

# Graph

@app.route("/graph.png", methods=("POST", "GET"))
def graph():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
    

def create_figure():
    sales = df["sales"]
    expenditure = df["expenditure"]
    months = df["month"]

    fig, ax = plt.subplots()
    ax.set_title("Monthly Sales and Expenditures")
    ax.set_xlabel("Months")
    ax.set_ylabel("Sale  + Expenditure ")


    plt.plot(months, sales, label = "sales")
    plt.plot(months, expenditure, label = "expenditure")
    plt.legend()

    return fig

       
if __name__=="__main__":
    app.run(debug=True)

   