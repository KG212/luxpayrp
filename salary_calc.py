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
        (0, 1185, 0, 0),(1190, 1370, 0.08, -95),
        (1375, 1555, 0.09, -108.7125),(1560, 1735, 0.1, -124.26250),
        (1740, 1920, 0.11, -141.65,000),(1925, 2105, 0.12, -160.87500),
        (2110, 2295, 0.14, -203.00,000),(2300, 2485, 0.16, -248.95000),
        (2490, 2680, 0.18, -298.72500),(2685, 2870, 0.2, -352.32500),
        (2875, 3060, 0.22, -409.75000),(3065, 3250, 0.24, -471.00000),
        (3255, 3445, 0.26, -536.07500),(3450, 3635, 0.28, -604.97500),
        (3640, 3825, 0.3, -677.70000),(3830, 4015, 0.32, -754.25000),
        (4020, 4210, 0.34, -834.62500),(4215, 4400, 0.36, -918.82500),
        (4405, 4590, 0.38, -1006.85000),(4595, 9870, 0.39, -1052.77500),
        (9875, 14765, 0.4, -1151.50000),(14770, 19655, 0.41, -1299.15000),
        (19660, 999999999, 0.42, -1495.725)
    ],
    "Classe 1A": [
        (0, 2290, 0.0000, -0.00000),(2295, 2435, 0.1000, -229.00000),
        (2440, 2580, 0.1125, -259,46250),(2585, 2730, 0.1250, -291.76250),
        (2735, 2875, 0.1375, -325,90000),(2880, 3025, 0.1500, -361.87500),
        (3030, 3175, 0.1750, -437,50000),(3180, 3330, 0.2000, -516.95000),
        (3335, 3480, 0.2250, -600,22500),(3485, 3635, 0.2500, -687.32500),
        (3640, 3790, 0.2750, -778,25000),(3795, 3940, 0.3000, -873.00000),
        (3945, 4095, 0.3250, -971,57500),(4100, 4245, 0.3500, -1073.97500),
        (4250, 4400, 0.3750, -1180,20000),(4405, 9870, 0.3900, -1246.23000),
        (9875, 14765, 0.40, -1344.95500),(14770, 19655, 0.4100, -1492.60500),
        (19660, 9999999, 0.42, -1689.18000)
    ],
    "Classe 2": [
        (0,2290, 0.00, -0.00000),(2295,2655, 0.08, -183.20000),
        (2660,3025, 0.09, -209.77500),(3030,3390, 0.10, -240.02500),
        (3395,3760, 0.11, -273.95000),(3765,4125, 0.12, -311.55000),
        (4130,4510, 0.14, -394.10000),(4515,4890, 0.16, -484.30000),
        (4895,5275, 0.18, -582.15000),(5280,5655, 0.20, -687.65000),
        (5660,6040, 0.22, -800.80000),(6045,6420, 0.24, -921.60000),
        (6425,6805, 0.26, -1050.05000),(6810,7185, 0.28, -1186.15000),
        (7190,7570, 0.30, -1329.90000),(7575,7950, 0.32, -1481.30000),
        (7955,8335, 0.34, -1640.35000),(8340,8715, 0.36, -1807.05000),
        (8720,9100, 0.38, -1981.40000),(9105,19660, 0.39, -2072.40000),
        (19665,29445, 0.40, -2269.00000),(29450,39230, 0.41, -2563.45000),
        (39235,9999999, 0.42, -2955.75000)
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