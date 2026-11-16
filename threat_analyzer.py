def calculate_risk(severity):

    risk = {
        "Low":20,
        "Medium":50,
        "High":80,
        "Critical":100
    }

    return risk.get(severity,0)