import re

def moneyToFloat(money: str):
    try:
        return float(re.sub('[^\d.]', '', money))
    except:
        return float(0)