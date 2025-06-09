from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("data.csv")

    # Group and create chart
    grouped = df.groupby("Department")["Salary"].mean().reset_index()

    plt.figure(figsize=(6,4))
    plt.bar(grouped["Department"], grouped["Salary"], color='tomato')
    plt.title("Avg Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Salary")
    plt.tight_layout()
    plt.savefig("static/chart.png")
    plt.close()

    return render_template("index.html", tables=[df.to_html(classes="data", header="true")])

if __name__ == "__main__":
    app.run(debug=True)
