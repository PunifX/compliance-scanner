import requests
import sys
headers_name = ["Strict-Transport-Security","Content-Security-Policy","X-Frame-Options","X-Content-Type-Options","Referrer-Policy","X-XSS-Protection"]
list_checked = []
def check_header(domain):
    data = requests.get(domain)

    data_headers= data.headers
    for name in headers_name:
        #for key,value in data_headers.items():
        #    if name == key:
        #        list_checked.append(name)

        if name in data_headers:
            print("[PASS]\n",name)
        else:
            print("[FAIL]\n",name)
            

        


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