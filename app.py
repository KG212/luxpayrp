from flask import Flask, request, render_template
from salary_calc import calculate_salary, TRAVEL_DEDUCTIONS

app = Flask(__name__)

SOCIAL_CLASSES = ["Classe 1", "Classe 1A", "Classe 2"]
RESIDENCES = ["Select"] + list(TRAVEL_DEDUCTIONS.keys())

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/salary", methods=["GET", "POST"])
def salary():
    result = None
    error = None
    if request.method == "POST":
        try:
            gross = float(request.form["gross_salary"])
            car = float(request.form["car_cost"])
            residence = request.form["residence"]
            social_class = request.form["social_class"]
            if social_class not in SOCIAL_CLASSES:
                error = "Please select a valid social class."
            elif residence not in TRAVEL_DEDUCTIONS:
                error = "Please select a valid residence."
            else:
                result = calculate_salary(gross, car, residence, social_class)
        except ValueError:
            error = "Gross salary and car cost must be numeric."
    return render_template("index.html", result=result, error=error,
                           social_classes=SOCIAL_CLASSES, residences=RESIDENCES)

@app.route("/parental_leave")
def parental_leave():
    return render_template("parental_leave.html")

@app.route("/creche")
def creche():
    return render_template("creche.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)