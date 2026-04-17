import math

def myround(x, base=5):
    return int(base * round(float(x) / base))

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

TRAVEL_DEDUCTIONS = {
    "Beckerich": 99*(9-4)/12, "Bertrange": 99*(10-4)/12, "Bettembourg": 99*(20-4)/12,
    "Betzdorf": 99*(29-4)/12, "Bissen": 99*(16-4)/12, "Boulaide": 99*(26-4)/12,
    "Bourscheid": 99*(28-4)/12, "Colmar-Berg": 99*(19-4)/12, "Contern": 99*(22-4)/12,
    "Dalheim": 99*(26-4)/12, "Diekirch": 99*(27-4)/12, "Differdange": 99*(17-4)/12,
    "Dippach": 99*(9-4)/12, "Dudelange": 99*(23-4)/12, "Ell": 99*(13-4)/12,
    "Erpeldange": 99*(25-4)/12, "Esch-sur-Alzette": 99*(19-4)/12, "Esch-sur-Sûre": 99*(24-4)/12,
    "Ettelbruck": 99*(23-4)/12, "Feulen": 99*(22-4)/12, "Fischbach": 99*(19-4)/12,
    "Flaxweiler": 99*(28-4)/12, "Frisange": 99*(24-4)/12, "Garnich": 99*(6-4)/12,
    "Goesdorf": 99*(28-4)/12, "Grosbous": 99*(18-4)/12, "Habscht": 99*(5-4)/12,
    "Heffingen": 99*(24-4)/12, "Helperknapp": 99*(7-4)/12, "Hesperange": 99*(18-4)/12,
    "Junglinster": 99*(22-4)/12, "Käerjeng": 99*(12-4)/12, "Kayl": 99*(21-4)/12,
    "Kehlen": 99*(6-4)/12, "Kopstal": 99*(9-4)/12, "Lac de la Haute-Sûre": 99*(29-4)/12,
    "Larochette": 99*(23-4)/12, "Leudelange": 99*(14-4)/12, "Lintgen": 99*(14-4)/12,
    "Lorentzweiler": 99*(14-4)/12, "Luxembourg": 99*(15-4)/12, "Mamer": 99*(7-4)/12,
    "Mersch": 99*(14-4)/12, "Mertzig": 99*(19-4)/12, "Mondercange": 99*(16-4)/12,
    "Mondorf-les-Bains": 99*(29-4)/12, "Niederanven": 99*(21-4)/12, "Nommern": 99*(21-4)/12,
    "Pétange": 99*(13-4)/12, "Préizerdaul": 99*(14-4)/12, "Rambrouch": 99*(19-4)/12,
    "Reckange-sur-Mess": 99*(13-4)/12, "Redange/Attert": 99*(12-4)/12, "Roeser": 99*(20-4)/12,
    "Rumelange": 99*(24-4)/12, "Saeul": 99*(7-4)/12, "Sandweiler": 99*(20-4)/12,
    "Sanem": 99*(14-4)/12, "Schieren": 99*(21-4)/12, "Schifflange": 99*(19-4)/12,
    "Schuttrange": 99*(24-4)/12, "Steinfort": max(0, 99*(3-4)/12), "Steinsel": 99*(13-4)/12,
    "Strassen": 99*(10-4)/12, "Useldange": 99*(11-4)/12, "Vallée de l'Ernz": 99*(25-4)/12,
    "Vichten": 99*(15-4)/12, "Wahl": 99*(19-4)/12, "Waldbillig": 99*(28-4)/12,
    "Waldbredimus": 99*(27-4)/12, "Walferdange": 99*(13-4)/12, "Weiler-la-Tour": 99*(23-4)/12
}

def get_travel_deduction(residence):
    return TRAVEL_DEDUCTIONS.get(residence, 0.0)

TAX_BRACKETS = {
    "Classe 1": [
        (0, 1185, 0, 0, 1.07),(1190, 1370, 0.08, -95, 1.07),
        (1375, 1555, 0.09, -108.7125, 1.07),(1560, 1735, 0.1, -124.26250, 1.07),
        (1740, 1920, 0.11, -141.650, 1.07),(1925, 2105, 0.12, -160.87500, 1.07),
        (2110, 2295, 0.14, -203.000, 1.07),(2300, 2485, 0.16, -248.95000, 1.07),
        (2490, 2680, 0.18, -298.72500, 1.07),(2685, 2870, 0.2, -352.32500, 1.07),
        (2875, 3060, 0.22, -409.75000, 1.07),(3065, 3250, 0.24, -471.00000, 1.07),
        (3255, 3445, 0.26, -536.07500, 1.07),(3450, 3635, 0.28, -604.97500, 1.07),
        (3640, 3825, 0.3, -677.70000, 1.07),(3830, 4015, 0.32, -754.25000, 1.07),
        (4020, 4210, 0.34, -834.62500, 1.07),(4215, 4400, 0.36, -918.82500, 1.07),
        (4405, 4590, 0.38, -1006.85000, 1.07),(4595, 9870, 0.39, -1052.77500, 1.07),
        (9875, 14765, 0.4, -1151.50000, 1.07),(14770, 19655, 0.41, -1299.15000, 1.07),
        (19660, 999999999, 0.42, -1495.725, 1.07)
    ],
    "Classe 1A": [
        (0, 2290, 0.0000, -0.00000, 1.07),(2295, 2435, 0.1000, -229.00000, 1.07),
        (2440, 2580, 0.1125, -259.46250, 1.07),(2585, 2730, 0.1250, -291.76250, 1.07),
        (2735, 2875, 0.1375, -325.90000, 1.07),(2880, 3025, 0.1500, -361.87500, 1.07),
        (3030, 3175, 0.1750, -437.50000, 1.07),(3180, 3330, 0.2000, -516.95000, 1.07),
        (3335, 3480, 0.2250, -600.22500, 1.07),(3485, 3635, 0.2500, -687.32500, 1.07),
        (3640, 3790, 0.2750, -778.25000, 1.07),(3795, 3940, 0.3000, -873.00000, 1.07),
        (3945, 4095, 0.3250, -971.57500, 1.07),(4100, 4245, 0.3500, -1073.97500, 1.07),
        (4250, 4400, 0.3750, -1180.20000, 1.07),(4405, 9870, 0.3900, -1246.23000, 1.07),
        (9875, 14765, 0.40, -1344.95500, 1.07),(14770, 19655, 0.4100, -1492.60500, 1.07),
        (19660, 9999999, 0.42, -1689.18000, 1.07)
    ],
    "Classe 2": [
        (0,2290, 0.00, -0.00000, 1.07),(2295,2655, 0.08, -183.20000, 1.07),
        (2660,3025, 0.09, -209.77500, 1.07),(3030,3390, 0.10, -240.02500, 1.07),
        (3395,3760, 0.11, -273.95000, 1.07),(3765,4125, 0.12, -311.55000, 1.07),
        (4130,4510, 0.14, -394.10000, 1.07),(4515,4890, 0.16, -484.30000, 1.07),
        (4895,5275, 0.18, -582.15000, 1.07),(5280,5655, 0.20, -687.65000, 1.07),
        (5660,6040, 0.22, -800.80000, 1.07),(6045,6420, 0.24, -921.60000, 1.07),
        (6425,6805, 0.26, -1050.05000, 1.07),(6810,7185, 0.28, -1186.15000, 1.07),
        (7190,7570, 0.30, -1329.90000, 1.07),(7575,7950, 0.32, -1481.30000, 1.07),
        (7955,8335, 0.34, -1640.35000, 1.07),(8340,8715, 0.36, -1807.05000, 1.07),
        (8720,9100, 0.38, -1981.40000, 1.07),(9105,19660, 0.39, -2072.40000, 1.07),
        (19665,29445, 0.40, -2269.00000, 1.07),(29450,39230, 0.41, -2563.45000, 1.07),
        (39235,9999999, 0.42, -2955.75000, 1.07)
    ]
}

def calculate_tax(imposable, social_class):
    # Round to nearest 5 first — tax brackets are defined in 5-euro steps
    taxable = myround(imposable, base=5)
    brackets = TAX_BRACKETS.get(social_class, [])
    for lower, upper, rate, deduction, multiplier in brackets:
        if lower <= taxable <= upper:
            return (taxable * rate + deduction) * multiplier
    return 0.0

# SSM as of 1 January 2026 (index 968.04) — update on next indexation
SSM_NON_QUALIFIED  = 2703.74
PARENTAL_LEAVE_MIN = SSM_NON_QUALIFIED              # 1× SSM  = € 2 703.74
PARENTAL_LEAVE_MAX = round(SSM_NON_QUALIFIED * 5/3, 2)  # 5/3× SSM = € 4 506.23

LEAVE_TYPES = {
    "full_time":    {"label": "Full-time",    "reduction": 1.00, "duration_single": 4,  "duration_twins": 6},
    "part_time_50": {"label": "Part-time 50%","reduction": 0.50, "duration_single": 8,  "duration_twins": 12},
    "part_time_25": {"label": "Part-time 25%","reduction": 0.25, "duration_single": 16, "duration_twins": 20},
}

def _contributions(gross):
    """Return (maladie, maladie_espece, pension, total) for a given gross income."""
    maladie        = round(gross * 0.028,  2)
    maladie_espece = round(gross * 0.0025, 2)
    pension        = round(gross * 0.08,   2)
    return maladie, maladie_espece, pension, round(maladie + maladie_espece + pension, 2)

def calculate_parental_leave(avg_gross, leave_type, twins, social_class, residence):
    config    = LEAVE_TYPES[leave_type]
    reduction = config["reduction"]
    duration  = config["duration_twins"] if twins else config["duration_single"]

    # --- CAE indemnity (separate employer) ---
    # Base = avg salary clamped to [1×SSM, 5/3×SSM], then scaled by reduction rate
    base      = max(PARENTAL_LEAVE_MIN, min(avg_gross, PARENTAL_LEAVE_MAX))
    cae_gross = round(base * reduction, 2)

    cae_mal, cae_mal_e, cae_pen, cae_cot = _contributions(cae_gross)
    # CAE indemnity: no travel deduction (not commuting for this portion)
    cae_imposable = round(cae_gross - cae_cot, 2)

    # --- Employer salary (only for part-time leave) ---
    if leave_type == "full_time":
        emp_gross     = 0.0
        emp_mal = emp_mal_e = emp_pen = emp_cot = emp_frais = emp_imposable = 0.0
    else:
        emp_gross = round(avg_gross * (1 - reduction), 2)
        emp_mal, emp_mal_e, emp_pen, emp_cot = _contributions(emp_gross)
        emp_frais     = round(get_travel_deduction(residence), 2)
        emp_imposable = round(emp_gross - emp_cot - emp_frais, 2)

    # --- Combined tax (both sources form a single annual tax base) ---
    total_gross      = round(emp_gross + cae_gross, 2)
    total_cotisations = round(emp_cot + cae_cot, 2)
    total_imposable  = round(emp_imposable + cae_imposable, 2)
    total_year       = total_gross * 12

    assurance_dependance = round((total_gross - 535) * 0.014, 2)

    if total_year < 40000:
        cis = round(600 / 12, 2)
    elif total_year < 80000:
        cis = round((600 - (total_year - 40000) * 0.015) / 12, 2)
    else:
        cis = 0

    impot       = calculate_tax(total_imposable, social_class)
    net_monthly = round(total_gross - total_cotisations - round_down(impot, 1)
                        + cis - assurance_dependance, 2)
    net_total   = round(net_monthly * duration, 2)

    return {
        "avg_gross":          avg_gross,
        "leave_type":         leave_type,
        "leave_type_label":   config["label"],
        "duration":           duration,
        # Employer table
        "emp_gross":          emp_gross,
        "emp_maladie":        emp_mal,
        "emp_maladie_espece": emp_mal_e,
        "emp_pension":        emp_pen,
        "emp_cotisations":    emp_cot,
        "emp_frais":          emp_frais,
        "emp_imposable":      emp_imposable,
        # CAE table
        "cae_gross":          cae_gross,
        "cae_maladie":        cae_mal,
        "cae_maladie_espece": cae_mal_e,
        "cae_pension":        cae_pen,
        "cae_cotisations":    cae_cot,
        "cae_imposable":      cae_imposable,
        # Combined summary
        "total_gross":        total_gross,
        "total_cotisations":  total_cotisations,
        "total_imposable":    total_imposable,
        "assurance_dependance": assurance_dependance,
        "cis":                cis,
        "impot":              round_down(impot, 1),
        "net_monthly":        net_monthly,
        "net_total":          net_total,
        # SSM reference
        "ssm":                PARENTAL_LEAVE_MIN,
        "ssm_max":            PARENTAL_LEAVE_MAX,
    }

def calculate_salary(gross_salary, car_cost, residence, social_class):
    total = gross_salary + car_cost
    total_year = total * 12

    assurance_maladie = round(total * 0.028, 2)
    assurance_maladie_espece = round(gross_salary * 0.0025, 2)
    assurance_pension = round(total * 0.08, 2)
    cotisations_totales = round(assurance_maladie + assurance_maladie_espece + assurance_pension, 2)

    frais_deplacement = get_travel_deduction(residence)
    imposable = round(total - cotisations_totales - frais_deplacement, 2)
    assurance_dependance = round((total - 535) * 0.014, 2)

    if total_year < 40000:
        cis = round(600 / 12, 2)   # €600/year = €50/month
    elif total_year < 80000:
        cis = round((600 - (total_year - 40000) * 0.015) / 12, 2)
    else:
        cis = 0

    impot = calculate_tax(imposable, social_class)
    net = round(total - cotisations_totales - impot + cis - assurance_dependance, 2)

    deduc_ticket = 50.4
    restant = round(net - car_cost - deduc_ticket, 2)
    restant_year = round(restant * 12, 2)

    return {
        "gross_month": gross_salary,
        "car_cost": car_cost,
        "total_month": total,
        "total_year": total_year,
        "assurance_maladie": assurance_maladie,
        "assurance_maladie_espece": assurance_maladie_espece,
        "assurance_pension": assurance_pension,
        "cotisations_totales": cotisations_totales,
        "frais_deplacement": round(frais_deplacement, 2),
        "imposable": imposable,
        "assurance_dependance": assurance_dependance,
        "cis": cis,
        "impot": round_down(impot, 1),
        "net": net,
        "deduc_ticket": deduc_ticket,
        "restant": restant,
        "restant_year": restant_year
    }


# ─── CSA — Chèque-Service Accueil ────────────────────────────────────────────
# Barème applicable from January 2026 (SSM index 968.04)

CSA_STATE_MAX_SEA = 7.00   # € max state contribution / hour — SEA & Mini crèche
CSA_STATE_MAX_AP  = 5.40   # € max state contribution / hour — Assistant parental

# Each entry: list of 3 tranches → (cumulative_upper_hours, rate_ap, rate_sea)
# Hours are per week; rate applies from previous upper + 1 through this upper.
CSA_BAREME = {
    # ─ REVIS / Situation de précarité ─
    ("revis", 1): [(13, 0.00, 0.00), (21, 0.00, 0.00), (26, 0.50, 0.50)],
    ("revis", 2): [(13, 0.00, 0.00), (21, 0.00, 0.00), (26, 0.30, 0.30)],
    ("revis", 3): [(13, 0.00, 0.00), (21, 0.00, 0.00), (26, 0.15, 0.15)],
    ("revis", 4): [(13, 0.00, 0.00), (21, 0.00, 0.00), (26, 0.00, 0.00)],
    # ─ Revenu < 1.5× SSM ─
    ("lt1.5", 1): [(13, 0.00, 0.00), (21, 0.50, 0.50), (26, 0.50, 0.50)],
    ("lt1.5", 2): [(13, 0.00, 0.00), (21, 0.30, 0.30), (26, 0.30, 0.30)],
    ("lt1.5", 3): [(13, 0.00, 0.00), (21, 0.15, 0.15), (26, 0.15, 0.15)],
    ("lt1.5", 4): [(13, 0.00, 0.00), (21, 0.00, 0.00), (26, 0.00, 0.00)],
    # ─ Revenu < 2× SSM ─
    ("lt2",   1): [(13, 0.00, 0.00), (21, 1.00, 1.00), (26, 1.50, 1.50)],
    ("lt2",   2): [(13, 0.00, 0.00), (21, 0.70, 0.70), (26, 1.10, 1.10)],
    ("lt2",   3): [(13, 0.00, 0.00), (21, 0.35, 0.35), (26, 0.55, 0.55)],
    ("lt2",   4): [(13, 0.00, 0.00), (21, 0.00, 0.00), (26, 0.00, 0.00)],
    # ─ Revenu < 2.5× SSM ─
    ("lt2.5", 1): [(8,  0.00, 0.00), (21, 1.50, 1.50), (31, 2.50, 2.50)],
    ("lt2.5", 2): [(8,  0.00, 0.00), (21, 1.10, 1.10), (31, 1.80, 1.80)],
    ("lt2.5", 3): [(8,  0.00, 0.00), (21, 0.55, 0.55), (31, 0.90, 0.90)],
    ("lt2.5", 4): [(8,  0.00, 0.00), (21, 0.00, 0.00), (31, 0.00, 0.00)],
    # ─ Revenu < 3× SSM ─
    ("lt3",   1): [(8,  0.00, 0.00), (21, 2.00, 2.00), (31, 3.50, 3.50)],
    ("lt3",   2): [(8,  0.00, 0.00), (21, 1.50, 1.50), (31, 2.60, 2.60)],
    ("lt3",   3): [(8,  0.00, 0.00), (21, 0.75, 0.75), (31, 1.30, 1.30)],
    ("lt3",   4): [(8,  0.00, 0.00), (21, 0.00, 0.00), (31, 0.00, 0.00)],
    # ─ Revenu < 3.5× SSM ─
    ("lt3.5", 1): [(3,  0.00, 0.00), (21, 2.50, 2.50), (36, 4.50, 4.50)],
    ("lt3.5", 2): [(3,  0.00, 0.00), (21, 1.80, 1.80), (36, 3.30, 3.30)],
    ("lt3.5", 3): [(3,  0.00, 0.00), (21, 0.90, 0.90), (36, 1.65, 1.65)],
    ("lt3.5", 4): [(3,  0.00, 0.00), (21, 0.00, 0.00), (36, 0.00, 0.00)],
    # ─ Revenu < 4× SSM ─
    ("lt4",   1): [(3,  3.50, 3.50), (21, 3.50, 3.50), (36, 5.40, 5.50)],
    ("lt4",   2): [(3,  2.70, 2.70), (21, 2.70, 2.70), (36, 4.10, 4.10)],
    ("lt4",   3): [(3,  1.60, 1.60), (21, 1.60, 1.60), (36, 2.05, 2.05)],
    ("lt4",   4): [(3,  0.00, 0.00), (21, 0.00, 0.00), (36, 0.00, 0.00)],
    # ─ Revenu < 4.5× SSM ─
    ("lt4.5", 1): [(3,  4.00, 4.00), (21, 4.00, 4.00), (36, 5.40, 6.00)],
    ("lt4.5", 2): [(3,  3.20, 3.20), (21, 3.20, 3.20), (36, 4.80, 4.80)],
    ("lt4.5", 3): [(3,  2.10, 2.10), (21, 2.10, 2.10), (36, 2.40, 2.40)],
    ("lt4.5", 4): [(3,  0.00, 0.00), (21, 0.00, 0.00), (36, 0.00, 0.00)],
    # ─ Revenu ≥ 4.5× SSM or no income declared ─
    ("gte4.5",1): [(3,  4.00, 4.00), (21, 4.00, 4.00), (36, 5.40, 6.00)],
    ("gte4.5",2): [(3,  3.20, 3.20), (21, 3.20, 3.20), (36, 5.40, 5.60)],
    ("gte4.5",3): [(3,  2.10, 2.10), (21, 2.10, 2.10), (36, 2.80, 2.80)],
    ("gte4.5",4): [(3,  0.00, 0.00), (21, 0.00, 0.00), (36, 0.00, 0.00)],
}

# Meal rate per meal for young (pre-school) children
CSA_MEAL_RATE = {
    "revis":  0.00, "lt1.5": 0.50, "lt2":  1.00, "lt2.5": 1.50,
    "lt3":    2.00, "lt3.5": 2.00, "lt4":  2.00, "lt4.5": 2.00, "gte4.5": 2.00,
}

CSA_INCOME_LABELS = {
    "revis":  "REVIS / Situation de précarité",
    "lt1.5":  "Revenu < 1.5× SSM  (< € {:,.0f}/month)".format(1.5 * SSM_NON_QUALIFIED),
    "lt2":    "Revenu < 2× SSM  (< € {:,.0f}/month)".format(2.0 * SSM_NON_QUALIFIED),
    "lt2.5":  "Revenu < 2.5× SSM  (< € {:,.0f}/month)".format(2.5 * SSM_NON_QUALIFIED),
    "lt3":    "Revenu < 3× SSM  (< € {:,.0f}/month)".format(3.0 * SSM_NON_QUALIFIED),
    "lt3.5":  "Revenu < 3.5× SSM  (< € {:,.0f}/month)".format(3.5 * SSM_NON_QUALIFIED),
    "lt4":    "Revenu < 4× SSM  (< € {:,.0f}/month)".format(4.0 * SSM_NON_QUALIFIED),
    "lt4.5":  "Revenu < 4.5× SSM  (< € {:,.0f}/month)".format(4.5 * SSM_NON_QUALIFIED),
    "gte4.5": "Revenu ≥ 4.5× SSM  (≥ € {:,.0f}/month)".format(4.5 * SSM_NON_QUALIFIED),
}

def get_csa_income_category(monthly_taxable, revis=False):
    if revis:
        return "revis"
    s = SSM_NON_QUALIFIED
    if monthly_taxable < 1.5 * s: return "lt1.5"
    if monthly_taxable < 2.0 * s: return "lt2"
    if monthly_taxable < 2.5 * s: return "lt2.5"
    if monthly_taxable < 3.0 * s: return "lt3"
    if monthly_taxable < 3.5 * s: return "lt3.5"
    if monthly_taxable < 4.0 * s: return "lt4"
    if monthly_taxable < 4.5 * s: return "lt4.5"
    return "gte4.5"

def calculate_csa(monthly_taxable, n_children, structure_type, hours_per_week,
                  weeks_per_year=46, meals_per_week=0, revis=False):
    income_cat = get_csa_income_category(monthly_taxable, revis)
    child_key  = min(n_children, 4)
    tranches   = CSA_BAREME[(income_cat, child_key)]
    state_rate = CSA_STATE_MAX_SEA if structure_type == "sea" else CSA_STATE_MAX_AP

    # Cost per week — break down by tranche
    tranche_details   = []
    total_parent_week = 0.0
    prev_upper        = 0

    for i, (upper, rate_ap, rate_sea) in enumerate(tranches):
        rate            = rate_ap if structure_type == "ap" else rate_sea
        hours_in_tranche = max(0, min(hours_per_week, upper) - prev_upper)
        parent_cost     = round(hours_in_tranche * rate, 2)
        tranche_details.append({
            "label":    f"Tranche {i + 1}",
            "range":    f"{prev_upper + 1}–{upper} h/week",
            "hours":    hours_in_tranche,
            "rate":     rate,
            "cost":     parent_cost,
            "is_free":  rate == 0.0,
        })
        total_parent_week += parent_cost
        prev_upper = upper

    t3_max             = tranches[-1][0]
    unsubsidized_hours = max(0, hours_per_week - t3_max)
    covered_hours      = min(hours_per_week, t3_max)

    # Meals
    meal_rate          = CSA_MEAL_RATE.get(income_cat, 0.0)
    meal_cost_week     = round(meals_per_week * meal_rate, 2)

    total_parent_week  = round(total_parent_week, 2)
    wk_factor          = weeks_per_year / 12
    total_parent_month = round((total_parent_week + meal_cost_week) * wk_factor, 2)
    total_parent_year  = round((total_parent_week + meal_cost_week) * weeks_per_year, 2)

    # State max contribution estimate (for informational display)
    state_week         = round(covered_hours * state_rate, 2)
    state_month        = round(state_week * wk_factor, 2)

    return {
        "income_cat":           income_cat,
        "income_cat_label":     CSA_INCOME_LABELS[income_cat],
        "structure_type":       structure_type,
        "hours_per_week":       hours_per_week,
        "t3_max_hours":         t3_max,
        "unsubsidized_hours":   unsubsidized_hours,
        "tranche_details":      tranche_details,
        "total_parent_week":    total_parent_week,
        "meals_per_week":       meals_per_week,
        "meal_rate":            meal_rate,
        "meal_cost_week":       meal_cost_week,
        "total_parent_month":   total_parent_month,
        "total_parent_year":    total_parent_year,
        "state_rate_per_hour":  state_rate,
        "state_week":           state_week,
        "state_month":          state_month,
        "weeks_per_year":       weeks_per_year,
        "ssm":                  SSM_NON_QUALIFIED,
    }
