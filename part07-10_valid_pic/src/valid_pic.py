import re
from datetime import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False

    chars = list("0123456789ABCDEFHJKLMNPRSTUVWXY")
    valid_marker = ['-', '+', 'A']
    centuries = {'+': '18', '-': '19', 'A': '20'}

    parts = re.split(r"([-+A])", pic)
    date = parts[0]
    century_mark = parts[1]
    personal_identifier = parts[2][:-1]
    control_character = parts[2][-1]

    date_check = False
    century_mark_check = False
    control_character_check = False

    full_date = date[:4] + centuries[century_mark] + date[4:]
    try:
        datetime.strptime(full_date, "%d%m%Y")
        date_check = True
    except ValueError:
        pass

    if century_mark in valid_marker:
        century_mark_check = True

    control_character_cal = int(date + personal_identifier) % 31
    if control_character == chars[control_character_cal]:
        control_character_check = True

    return date_check and century_mark_check and control_character_check


if __name__ == "__main__":
    pics = ["110986+713J"]

    for pic in pics:
        print(is_it_valid(pic))