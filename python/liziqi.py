import requests
import sys
import time
from datetime import datetime

def count_subscriptions():
    URL = "https://api.bilibili.com/x/relation/stat?vmid="

    upid = "19577966"

    r = requests.get(url=URL + upid)

    data = r.json()
    return data["data"]["follower"]

def retrieve_subs():
    while 1:
        # dd/mm/YY
        d1 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        f = open("liziqi_subscription.txt", "a")
        f.write(str(d1) + "," + str(count_subscriptions()))
        f.write("\n")
        print(count_subscriptions())
        f.close()
        time.sleep(30)

def main_loop():
    retrieve_subs()



if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
