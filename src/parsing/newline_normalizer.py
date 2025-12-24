import re

def newline_normalize(str):
    rm_whitespace = re.sub(r'\s', ' ', str) # 공백문자
    rm_privmsg_1 = re.sub(r'[\uE000-\uF8FF]', '', rm_whitespace) # 사적문자 (1)
    rm_privmsg_2 = re.sub(r'[\U000F0000-\U000FFFFD]', '', rm_privmsg_1) # 사적문자 (2)

    return rm_privmsg_2