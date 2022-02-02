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

api_url = 'https://api.telegram.org/bot<bot_auth_key>/sendMessage?chat_id=<group_ID>&text='

# Original Time table
# timetable = {
#     0:{time(10, 15):'43', time(14, 15):'45', time(15, 15):'42', time(16, 15):'43'},
#     1:{time(10, 15):'44', time(14, 15):'45', time(15, 15):'41', time(16, 15):'44'},
#     2:{time(10, 15):'46', time(14, 15):'45', time(15, 15):'43', time(16, 15):'42'},
#     3:{time(10, 15):'42', time(14, 15):'42', time(15, 15):'44', time(16, 15):'41'},
#     4:{time(10, 15):'47', time(14, 15):'41', time(15, 15):'43', time(16, 15):'44'},
#     5:{time(11, 30):'47', time(14, 15):'47'}
# }

# Out of Syllabus Time table
timetable = {
    0:{time(10, 15):'43', time(12, 15):'42', time(14, 15):'45', time(16, 15):'43'},
    1:{time(10, 15):'44', time(12, 15):'42', time(14, 15):'45', time(15, 15):'41', time(16, 15):'44'},
    2:{time(10, 15):'46', time(12, 15):'42', time(14, 15):'45', time(15, 15):'43'},
    3:{time(15, 15):'44', time(16, 15):'41'},
    4:{time(10, 15):'47', time(14, 15):'41', time(15, 15):'43', time(16, 15):'44'},
    5:{time(11, 30):'47', time(14, 15):'47'}
}
sub_codes = {41:'Operating Systems',
             42:'Out of TimeTable DBMS',
             43:'Intro to ML',
             44:'ADA',
             45:'Maths-II',
             46:'Python',
             47:'Internship'}
meeting_links = {
                 41:'https://meet.google.com/vyc-sohu-bpk?authuser=1',
                 42:'https://bit.ly/3nvLe5y',
                 43:'https://meet.google.com/vsq-szre-okn?authuser=1',
                 44:'https://meet.google.com/kiz-wnzj-wcr?authuser=1&hs=179',
                 45:'ओह नौ शीट। 🤷',
                 46:'https://bit.ly/3nvLe5y',
                 47:'https://meet.google.com/pcc-drdp-jod?authuser=1&hs=179'
                 }

_10_15 = time(10, 15)
_12_15 = time(12, 15)
_2_15 = time(14, 15)
_3_15 = time(15, 15)
_4_15 = time(16, 15)
_5_30 = time(17, 30)
text = f"Today's classes\n"

for key, value in timetable.items():
    if key == today.weekday():
        for key1, value1 in value.items():
            text = text + f"{key1.strftime('%I:%M:%p')} - {sub_codes[int(value1)]}\n"
if today.weekday() != 6:
    requests.get(api_url + text)



while """datetime.time(datetime.now(pytz.timezone('Asia/Kolkata'))) > _10_15""" and datetime.time(datetime.now(pytz.timezone('Asia/Kolkata'))) < _5_30:
    CurrentTime = datetime.time(datetime.now(pytz.timezone('Asia/Kolkata')))
    for key, value in timetable.items():
        if key == today.weekday():
            if CurrentTime >= _10_15 and a1:
                a1 = False
                text = f"{sub_codes[int(value[_10_15])]}\nLink:- {meeting_links[int(value[_10_15])]}"
                requests.get(api_url + text)
            elif CurrentTime >= _12_15 and a2 and (today.weekday()==4 or today.weekday()==5):
                a2 = False
                text = f"{sub_codes[int(value[_11_30])]}\nLink:- {meeting_links[int(value[_11_30])]}"
                requests.get(api_url + text)
            elif CurrentTime >= _2_15 and a3:
                a3 = False
                text = f"{sub_codes[int(value[_2_15])]}\nLink:- {meeting_links[int(value[_2_15])]}"
                requests.get(api_url + text)
            elif CurrentTime >= _3_15 and a4:
                a4 = False
                text = f"{sub_codes[int(value[_3_15])]}\nLink:- {meeting_links[int(value[_3_15])]}"
                requests.get(api_url + text)
            elif CurrentTime >= _4_15 and a5:
                a5 = False
                text = f"{sub_codes[int(value[_4_15])]}\nLink:- {meeting_links[int(value[_4_15])]}"
                requests.get(api_url + text)
                break
    t.sleep(3)            


