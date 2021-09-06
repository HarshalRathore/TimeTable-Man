from datetime import datetime, time, date
import pytz
import requests
import time as t

today = date.today()


a1 = True
a2 = True
a3 = True
a4 = True
a5 = True
a6 = True

api_url = 'https://api.telegram.org/bot<Bot_authentication_key>/sendMessage?chat_id=<group_chat_id>&text='


timetable = {
    0:{time(10, 30):'36', time(14, 00):'35', time(15, 15):'32', time(16, 30):'34'},
    1:{time(10, 30):'32', time(14, 00):'32', time(15, 15):'33', time(16, 30):'31'},
    2:{time(10, 30):'34', time(14, 00):'35', time(15, 15):'31', time(16, 30):'34'},
    3:{time(10, 30):'33', time(14, 00):'35', time(15, 15):'31', time(16, 30):'33'},
    4:{time(10, 30):'37', time(11, 30):'31', time(14, 00):'34', time(15, 15):'32', time(16, 30):'33'},
    5:{time(11, 30):'37', time(14, 00):'37'}
}

sub_codes = {31:'Managerial Economics',
             32:'Intro to Data Science',
             33:'DSALGO',
             34:'COA',
             35:'Discrete Mathematics',
             36:'Language Lab',
             37:'Evaluation of Internship'}
meeting_links = {
                 31:'https://meet.google.com/lookup',
                 32:'https://meet.google.com/lookup',
                 33:'https://meet.google.com/lookup',
                 34:'https://meet.google.com/lookup',
                 35:'https://meet.google.com/lookup',
                 36:'https://meet.google.com/lookup',
                 37:'No link provided'
                 }

_10_30 = time(10, 30)
_11_30 = time(11, 30)
_2_00 = time(14, 00)
_3_15 = time(15, 15)
_4_30 = time(16, 30)
_5_30 = time(17, 30)
text = f"Today's classes\n"

for key, value in timetable.items():
    if key == today.weekday():
        for key1, value1 in value.items():
            text = text + f"{key1.strftime('%I:%M:%p')} - {sub_codes[int(value1)]}\n"
if today.weekday() != 6:
    requests.get(api_url + text)



while """datetime.time(datetime.now(pytz.timezone('Asia/Kolkata'))) > _10_30""" and datetime.time(datetime.now(pytz.timezone('Asia/Kolkata'))) < _5_30:
    currtime = datetime.time(datetime.now(pytz.timezone('Asia/Kolkata')))
    for key, value in timetable.items():
        if key == today.weekday():
            if currtime >= _10_30 and a1:
                a1 = False
                text = f"{sub_codes[int(value[_10_30])]}\nLink:- {meeting_links[int(value[_10_30])]}"
                requests.get(api_url + text)
            elif currtime >= _11_30 and a2 and (today.weekday()==4 or today.weekday()==5):
                a2 = False
                text = f"{sub_codes[int(value[_11_30])]}\nLink:- {meeting_links[int(value[_11_30])]}"
                requests.get(api_url + text)
            elif currtime >= _2_00 and a3:
                a3 = False
                text = f"{sub_codes[int(value[_2_00])]}\nLink:- {meeting_links[int(value[_2_00])]}"
                requests.get(api_url + text)
            elif currtime >= _3_15 and a4:
                a4 = False
                text = f"{sub_codes[int(value[_3_15])]}\nLink:- {meeting_links[int(value[_3_15])]}"
                requests.get(api_url + text)
            elif currtime >= _4_30 and a5:
                a5 = False
                text = f"{sub_codes[int(value[_4_30])]}\nLink:- {meeting_links[int(value[_4_30])]}"
                requests.get(api_url + text)
                break
    t.sleep(300)            


