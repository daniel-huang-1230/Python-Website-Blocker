import time
from datetime import datetime as dt
hosts_path = r"/etc/hosts"   # r is for raw string
redirect = "127.0.0.1"
web_sites_list = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 21):
        print("Working hours")

    else:
        print("Fun time")
    time.sleep(5)