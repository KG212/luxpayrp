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
    "Schuttrange": 99*(24-4)/12, "Steinfort": 99*(3-4)/12, "Steinsel": 99*(13-4)/12,
    "Strassen": 99*(10-4)/12, "Useldange": 99*(11-4)/12, "Vallée de l’Ernz": 99*(25-4)/12,
    "Vichten": 99*(15-4)/12, "Wahl": 99*(19-4)/12, "Waldbillig": 99*(28-4)/12,
    "Waldbredimus": 99*(27-4)/12, "Walferdange": 99*(13-4)/12, "Weiler-la-Tour": 99*(23-4)/12
}

def get_travel_deduction(residence):
    return TRAVEL_DEDUCTIONS.get(residence, 0.0)

TAX_BRACKETS = {
    "Classe 1": [
        (0, 1020, 0.00, 0.00, 1.07), (1025, 1175, 0.08, -81.90, 1.07),
        (1180, 1335, 0.09, -93.6975, 1.07), (1340, 1490, 0.10, -107.055, 1.07),
        (1495, 1645, 0.11, -121.9725, 1.07), (1650, 1800, 0.12, -138.45, 1.07),
        (1805, 1965, 0.14, -174.525, 1.07), (1970, 2125, 0.16, -213.84, 1.07),
        (2130, 2285, 0.18, -256.395, 1.07), (2290, 2450, 0.20, -302.19, 1.07),
        (2455, 2610, 0.22, -351.225, 1.07), (2615, 2775, 0.24, -403.5, 1.07),
        (2780, 2935, 0.26, -459.015, 1.07), (2940, 3095, 0.28, -517.77, 1.07),
        (3100, 3260, 0.30, -579.765, 1.07), (3265, 3420, 0.32, -645.00, 1.00),
        (3425, 3585, 0.34, -713.475, 1.07), (3590, 3745, 0.36, -785.19, 1.07),
        (3750, 3905, 0.38, -860.145, 1.07), (3910, 8415, 0.39, -899.2425, 1.07),
        (8420, 12585, 0.40, -983.4275, 1.07), (12590, 16750, 0.41, -1109.2775, 1.07),
        (16755, 9999999.99, 0.42, -1276.7975, 1.07)
    ],
    "Classe 1A": [
        (0, 1960, 0.00, 0.00, 1.07), (1965, 2065, 0.12, -235.50, 1.07),
        (2070, 2170, 0.135, -266.475, 1.07), (2175, 2270, 0.15, -299.055, 1.07),
        (2275, 2375, 0.165, -333.1725, 1.07), (2380, 2480, 0.18, -368.85, 1.07),
        (2485, 2590, 0.21, -443.325, 1.07), (2595, 2695, 0.24, -521.04, 1.07),
        (2700, 2805, 0.27, -601.995, 1.07), (2810, 2910, 0.30, -686.19, 1.07),
        (2915, 3020, 0.33, -773.625, 1.07), (3025, 3130, 0.36, -864.30, 1.07),
        (3135, 8415, 0.39, -958.215, 1.07), (8420, 12585, 0.40, -1042.40, 1.07),
        (12590, 16750, 0.41, -1168.25, 1.07), (16755, 9999999.99, 0.42, -1335.77, 1.07)
    ],
    "Classe 2": [
        (0, 1960, 0.00, 0.00, 1.07), (1965, 2270, 0.08, -157.00, 1.07),
        (2275, 2585, 0.09, -179.745, 1.07), (2590, 2895, 0.10, -205.61, 1.07),
        (2900, 3210, 0.11, -234.595, 1.07), (3215, 3520, 0.12, -266.70, 1.07),
        (3525, 3845, 0.14, -337.15, 1.07), (3850, 4170, 0.16, -414.08, 1.07),
        (4175, 4490, 0.18, -497.49, 1.07), (4495, 4815, 0.20, -587.38, 1.07),
        (4820, 5140, 0.22, -683.75, 1.07), (5145, 5465, 0.24, -786.60, 1.07),
        (5470, 5790, 0.26, -895.93, 1.07), (5795, 6110, 0.28, -1011.74, 1.07),
        (6115, 6435, 0.30, -1134.03, 1.07), (6440, 6760, 0.32, -1262.80, 1.07),
        (6765, 7085, 0.34, -1398.05, 1.07), (7090, 7410, 0.36, -1539.78, 1.07),
        (7415, 7730, 0.38, -1687.99, 1.07), (7735, 16750, 0.39, -1765.335, 1.07),
        (16755, 25085, 0.40, -1932.855, 1.07), (25090, 33415, 0.41, -2183.705, 1.07),
        (33420, 9999999.99, 0.42, -2517.895, 1.07)
    ]
}

def calculate_tax(imposable, social_class):
    brackets = TAX_BRACKETS.get(social_class, [])
    for lower, upper, rate, deduction, multiplier in brackets:
        if lower <= imposable <= upper:
            return (myround(imposable, base=5) * rate + deduction) * multiplier
    return 0.0

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
        cis = 600
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