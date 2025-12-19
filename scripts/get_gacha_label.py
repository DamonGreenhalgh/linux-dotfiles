import json
import datetime
import sys

db = {
    "hsr": {
        "start_date": '20230426',
        "start_version": '1.0',
        "class": "hsr",
        "short": "HSR",
        "label": "Honkai: Star Rail",
        "cycle_period": 42, 
        "version_capstones": ['1.6', '2.7', '3.8'],
        # extra flair
        "flair": 'Memories are the Prelude to Dreams'
    },
    "zzz": {
        "start_date": '20240704',
        "start_version": "1.0",
        "class": "zzz",
        "short": "ZZZ",
        "label": "Zenless Zone Zero",
        "cycle_period": 42,
        "version_capstones": ['1.7'],
        "flair": "To Be Fuel for the Night"
    },
    "wuwa": {
        "start_date": "20251120",
        "start_version": "2.8",
        "class": "wuwa",
        "short": "WUWA",
        "label": "Wuthering Waves",
        "cycle_period": 35,    # Update after patch back to 42
        "version_capstones": ['1.4', '2.8'],
        "flair": "We Who See the Stars"
    }
}

data = db[sys.argv[1]]    # first arg is the type
start_date = datetime.date(
    int(data['start_date'][:4]), 
    int(data['start_date'][4:6]),
    int(data['start_date'][6:])
)
current_date = datetime.date.today()
version = data['start_version']
next_date = start_date

while (next_date - current_date).days < 0:
    # increment to next version
    next_date = next_date + datetime.timedelta(days=data['cycle_period'])
    if version in data['version_capstones']:
        # increment major version
        version = str(int(version[0]) + 1) + '.0'
    else:
        # increment minor version
        version = version[:2] + str(int(version[2:]) + 1)
        
days_remaining = (next_date - current_date).days
result = {
    "text": f"{data['short']} {version} ~ {days_remaining} day{'s' if days_remaining > 1 else ''}",
    "alt": f"{data['short']} {version} {data['flair']} ~ {days_remaining} day{'s' if days_remaining > 1 else ''} remaining",
    "class": ["chip", data['class']]
}
print(json.dumps(result))
