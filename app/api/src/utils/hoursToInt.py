import re

def hoursToInt(hour: str):
    try:
        return int(re.sub('\D', '', hour))
    except:
        return 0