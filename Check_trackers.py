import requests
import sys
from bs4 import BeautifulSoup
tracker_domains = ["google-analytics.com", "googletagmanager.com", "facebook.net", "fbevents.js", "hotjar.com", "doubleclick.net", "googlesyndication.com", "twitter.com/uwt.js", "snap.licdn.com", "bat.bing.com", "analytics.tiktok.com", "cdn.mxpnl.com"]
def Check_tracker(domain):
    tracker_found = False
    tracker_list = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}

    data = requests.get(domain,headers=headers)
    soup = BeautifulSoup(data.text,"html.parser")
    scripts = soup.find_all('script',src=True)
    for script in scripts:
        script = script["src"]
        for tracker in tracker_domains:
            if tracker in script:
                tracker_found=True
                tracker_list.append(tracker)
    
    if tracker_found:
        print("[FAIL] there is a tracker")
        print(tracker_list)
    if not tracker_found:
        print("[PASS] there is no tracker")


if len(sys.argv) > 1:
    domain = str(sys.argv[1])
    if not domain.startswith("https://") and not domain.startswith("http://"):
        domain = "http://" + domain
        Check_tracker(domain)
    else:
        Check_tracker(domain)
else:
    print("Please enter a domain")
    sys.exit(1)    