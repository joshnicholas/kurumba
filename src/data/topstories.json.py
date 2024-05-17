import json
import requests
import sys

urlos = {"google_top":'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/google_top/latest.json',
"google_search": 'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/google/latest.json',
"abc": 'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/abc_top/latest.json',
"sbs":'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/sbs_top/latest.json',
"graun":'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/graun_top/latest.json',
"smh": 'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/smh_top/latest.json',
"age": 'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/age/latest.json',
"brisbane_times": 'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/brisbane_times/latest.json',
"new":'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/newscom_top/latest.json',
"tech_meme":'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/tech_meme_top/latest.json',
"wiki": 'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/wiki/latest.json'}

resulto = {} 

for keyo in urlos.keys():
    resulto[keyo] = requests.get(urlos[keyo]).json()

json.dump(resulto, sys.stdout)

