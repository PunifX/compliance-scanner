import requests
import sys

def check_header(domain):
    data = requests.get(domain)

    data_headers= data.headers
    
    for key,value in data_headers.items():
        print(key,"",value)



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