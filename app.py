from flask import Flask, request, render_template
from salary_calc import (calculate_salary, calculate_parental_leave,
                         TRAVEL_DEDUCTIONS, LEAVE_TYPES)

app = Flask(__name__)

@app.template_filter("currency")
def currency_filter(value):
    return f"€ {value:,.2f}"

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
            if gross <= 0:
                error = "Gross salary must be a positive number."
            elif car < 0:
                error = "Car benefit cannot be negative."
            elif social_class not in SOCIAL_CLASSES:
                error = "Please select a valid social class."
            elif residence not in TRAVEL_DEDUCTIONS:
                error = "Please select a valid residence."
            else:
                result = calculate_salary(gross, car, residence, social_class)
        except ValueError:
            error = "Gross salary and car cost must be numeric."
    return render_template("index.html", result=result, error=error,
                           social_classes=SOCIAL_CLASSES, residences=RESIDENCES)

@app.route("/parental_leave", methods=["GET", "POST"])
def parental_leave():
    result = None
    error = None
    if request.method == "POST":
        try:
            avg_gross   = float(request.form["avg_gross"])
            leave_type  = request.form["leave_type"]
            twins       = request.form.get("twins") == "yes"
            social_class = request.form["social_class"]
            residence   = request.form["residence"]
            if avg_gross <= 0:
                error = "Average salary must be a positive number."
            elif leave_type not in LEAVE_TYPES:
                error = "Please select a valid leave type."
            elif social_class not in SOCIAL_CLASSES:
                error = "Please select a valid social class."
            elif residence not in TRAVEL_DEDUCTIONS:
                error = "Please select a valid residence."
            else:
                result = calculate_parental_leave(avg_gross, leave_type, twins,
                                                  social_class, residence)
        except ValueError:
            error = "Average salary must be a numeric value."
    return render_template("parental_leave.html", result=result, error=error,
                           leave_types=LEAVE_TYPES, social_classes=SOCIAL_CLASSES,
                           residences=RESIDENCES)

@app.route("/creche")
def creche():
    return render_template("creche.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)