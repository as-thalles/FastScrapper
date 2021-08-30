from typing import Dict, List
import datetime as _dt
import json as _json


PATH_DATASOURCE = './../events.json'

def get_all_events() -> Dict:
    with open(PATH_DATASOURCE) as events_file:
        data = _json.load(events_file)
    
    return data


def get_events_today() -> List:
    today = _dt.date.today()
    month = today.strftime('%B')
    return get_events_by_date(month, today.day)


def get_events_by_month(month:str) -> Dict:
    events = get_all_events()
    try:
        month_events = events[month.lower()]
        return month_events
    except KeyError:
        return 'Invalid month: ' + month


def get_events_by_date(month:str, day:int) -> List:
    try:
        month_events = get_events_by_month(month)
    except KeyError:
        return 'Invalid month: ' + month

    try:
        day_events = month_events[str(day)]
        return day_events
    except KeyError:
        return 'Invalid day: ' + day
