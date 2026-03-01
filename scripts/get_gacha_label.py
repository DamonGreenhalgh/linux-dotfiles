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
}

current_date = datetime.date.today()

result = {
    "text": "   ... . . / -.-- --- ..- / - --- -- --- .-. .-. --- .--",
    "alt": "HSR",
    "class": ["chip", "hsr"]
}
print(json.dumps(result))
