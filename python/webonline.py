import requests
import sys
import time
from datetime import datetime

def count_webonline():
    URL = "https://api.bilibili.com/x/web-interface/online?&"

    r = requests.get(url=URL)

    data = r.json()
    return data["data"]["web_online"]

def retrieve_subs():
    while 1:
        # dd/mm/YY
        d1 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        f = open("webonline_count.txt", "a")
        f.write(str(d1) + "," + str(count_webonline()))
        f.write("\n")
        f.close()
        time.sleep(30)

if __name__ == '__main__':
    try:
        retrieve_subs()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
