import math

def myround(x, base=5):
    return int(base * round(float(x)/base))

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

# Travel deduction mapping
TRAVEL_DEDUCTIONS = {
    "Beckerich": 99*(9-4)/12,
    "Bertrange": 99*(10-4)/12,
    # … continue mapping all cities …
}

def get_travel_deduction(residence):
    return TRAVEL_DEDUCTIONS.get(residence, 0)

# Tax brackets (simplified example, you’ll fill in full tables)
TAX_BRACKETS = {
    "Classe 1": [
        (0, 1020, 0, 0, 1.07),
        (1025, 1175, 0.08, -81.90, 1.07),
        # … continue …
    ],
    "Classe 1A": [
        (0, 1960, 0, 0, 1.07),
        (1965, 2065, 0.12, -235.50, 1.07),
        # … continue …
    ],
    "Classe 2": [
        (0, 1960, 0, 0, 1.07),
        (1965, 2270, 0.08, -157.00, 1.07),
        # … continue …
    ]
}

def calculate_tax(imposable, social_class):
    brackets = TAX_BRACKETS.get(social_class, [])
    for lower, upper, rate, deduction, multiplier in brackets:
        if lower <= imposable <= upper:
            return (myround(imposable, base=5) * rate + deduction) * multiplier
    return 0

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

    # CIS deduction
    if total_year < 40000:
        cis = 600
    elif total_year < 80000:
        cis = round((600 - (total_year - 40000) * 0.015) / 12, 2)
    else:
        cis = 0

    # Tax
    impot = calculate_tax(imposable, social_class)

    # Net salary
    net = round(total - cotisations_totales - impot + cis - assurance_dependance, 2)

    # Ticket + car deductions
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
        "frais_deplacement": frais_deplacement,
        "imposable": imposable,
        "assurance_dependance": assurance_dependance,
        "cis": cis,
        "impot": round_down(impot, 1),
        "net": net,
        "deduc_ticket": deduc_ticket,
        "restant": restant,
        "restant_year": restant_year
    }