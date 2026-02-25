import sys
import requests

def Check_Cookies(domain):
    data = requests.get(domain)
    for cookie in data.cookies:
        print(cookie.name,cookie.value)


if len(sys.argv) > 1:
    domain = str(sys.argv[1])
    if not domain.startswith("https://") and not domain.startswith("http://"):
        domain = "http://" + domain
        Check_Cookies(domain)
    else:
        Check_Cookies(domain)
else:
    print("Please enter a domain")
    sys.exit(1)    