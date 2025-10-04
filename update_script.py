# update_script.py
import datetime
import pytz
import random

TIMEZONE = 'America/New_York'
WORK_HOURS = (datetime.time(9, 0), datetime.time(17, 0))
BREAKS = [
    (datetime.time(10, 30), datetime.time(10, 45)),
    (datetime.time(12, 0), datetime.time(12, 30)),
    (datetime.time(14, 30), datetime.time(14, 45))
]
COMMIT_CHANCE = 0.3

def should_commit_now():
    now = datetime.datetime.now(pytz.timezone(TIMEZONE))
    
    # *** CTF Override: Weekend check commented out to allow run on Saturday ***
    # if now.weekday() >= 5 or not (WORK_HOURS[0] <= now.time() < WORK_HOURS[1]):
    if not (WORK_HOURS[0] <= now.time() < WORK_HOURS[1]):
        return False
    
    for start, end in BREAKS:
        if start <= now.time() < end:
            return False
            
    return random.random() < COMMIT_CHANCE

if __name__ == "__main__":
    if should_commit_now():
        print("ACTION: Make commit.")

