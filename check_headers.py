import requests
import sys

def check_header(domain):
    data = requests.get(domain)

    


if len(sys.argv) > 1:

    domain = sys.argv[1]
    if not domain.startswith("https://") and not domain.startswith("http://"):
        domain = "http://" + domain
        check_header(domain)
    else:
        check_header(domain)
else:
    print("please enter a domain")
    sys.exit(1)