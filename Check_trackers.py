import requests
import sys
from bs4 import BeautifulSoup

def Check_tracker(domain):
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}

    data = requests.get(domain,headers=headers)
    soup = BeautifulSoup(data,'html.parser')
    script = soup.find_all('script',src=True)
    print(script)


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