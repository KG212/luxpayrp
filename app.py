from flask import Flask, request, render_template
from salary_calc import calculate_salary

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        gross = float(request.form["gross_salary"])
        car = float(request.form["car_cost"])
        residence = request.form["residence"]
        social_class = request.form["social_class"]
        result = calculate_salary(gross, car, residence, social_class)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)