import time
import datetime
from dateutil.relativedelta import relativedelta

current_milli_time = lambda: int(round(time.time()*1000))

def next_date_frm_epoch(s,offset=None):
    if not offset:
        return datetime.datetime.fromtimestamp(s)
    temp = datetime.datetime.fromtimestamp(s)
    next_date = temp + relativedelta(months=offset)
    return next_date

def datetime_from_s(seconds=None):
    if seconds:
        return datetime.datetime.fromtimestamp(float(seconds))
    return seconds

