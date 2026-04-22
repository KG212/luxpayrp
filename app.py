from flask import Flask, request, render_template, session, redirect, url_for
from salary_calc import (calculate_salary, calculate_parental_leave, calculate_csa,
                         LEAVE_TYPES, SSM_NON_QUALIFIED)
from translations import TRANSLATIONS

app = Flask(__name__)
app.secret_key = 'luxpay-2026-change-in-production'


@app.template_filter("currency")
def currency_filter(value):
    return f"€ {value:,.2f}"


@app.context_processor
def inject_translations():
    lang = session.get('lang', 'fr')
    return {'t': TRANSLATIONS[lang], 'lang': lang}


@app.route('/set_lang/<lang>')
def set_lang(lang):
    if lang in TRANSLATIONS:
        session['lang'] = lang
    return redirect(request.referrer or url_for('home'))


SOCIAL_CLASSES = ["Classe 1", "Classe 1A", "Classe 2"]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/salary", methods=["GET", "POST"])
def salary():
    result    = None
    error_key = None
    if request.method == "POST":
        try:
            gross        = float(request.form["gross_salary"])
            car          = float(request.form.get("car_cost") or "0")
            social_class = request.form["social_class"]
            compute_frais     = request.form.get("compute_frais") == "yes"
            ticket_restaurant = request.form.get("ticket_restaurant") == "yes"
            frais_amount      = 0.0
            if compute_frais:
                try:
                    frais_amount = float(request.form.get("frais_amount") or "0")
                except ValueError:
                    frais_amount = 0.0

            if gross <= 0:
                error_key = "err_gross_pos"
            elif car < 0:
                error_key = "err_car_neg"
            elif social_class not in SOCIAL_CLASSES:
                error_key = "err_class"
            else:
                result = calculate_salary(gross, car, frais_amount, social_class,
                                          ticket_restaurant)
                result['compute_frais'] = compute_frais
        except ValueError:
            error_key = "err_numeric"
    return render_template("index.html", result=result, error_key=error_key,
                           social_classes=SOCIAL_CLASSES)


@app.route("/parental_leave", methods=["GET", "POST"])
def parental_leave():
    result    = None
    error_key = None
    if request.method == "POST":
        try:
            avg_gross    = float(request.form["avg_gross"])
            leave_type   = request.form["leave_type"]
            twins        = request.form.get("twins") == "yes"
            social_class = request.form["social_class"]

            if avg_gross <= 0:
                error_key = "err_avg_gross"
            elif leave_type not in LEAVE_TYPES:
                error_key = "err_leave_type"
            elif social_class not in SOCIAL_CLASSES:
                error_key = "err_class"
            else:
                result = calculate_parental_leave(avg_gross, leave_type, twins,
                                                  social_class)
        except ValueError:
            error_key = "err_avg_numeric"
    return render_template("parental_leave.html", result=result, error_key=error_key,
                           leave_types=LEAVE_TYPES, social_classes=SOCIAL_CLASSES)


@app.route("/creche", methods=["GET", "POST"])
def creche():
    result    = None
    error_key = None
    if request.method == "POST":
        try:
            revis                = request.form.get("revis") == "yes"
            monthly_taxable      = 0.0 if revis else float(request.form["monthly_taxable"])
            n_children           = int(request.form["n_children"])
            structure_type       = request.form["structure_type"]
            hours_per_week       = float(request.form["hours_per_week"])
            weeks_per_year       = int(request.form.get("weeks_per_year", 46))
            meals_per_week       = int(request.form.get("meals_per_week", 0))
            _shr                 = request.form.get("structure_hourly_rate", "").strip()
            structure_hourly_rate = float(_shr) if _shr else None

            if not revis and monthly_taxable <= 0:
                error_key = "err_income_pos"
            elif hours_per_week <= 0 or hours_per_week > 60:
                error_key = "err_hours"
            elif weeks_per_year < 1 or weeks_per_year > 52:
                error_key = "err_weeks"
            else:
                result = calculate_csa(monthly_taxable, n_children, structure_type,
                                       hours_per_week, weeks_per_year, meals_per_week, revis,
                                       structure_hourly_rate)
        except ValueError:
            error_key = "err_fields"
    return render_template("creche.html", result=result, error_key=error_key,
                           ssm=SSM_NON_QUALIFIED)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
