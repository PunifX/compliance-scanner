import requests
import sys
headers_name = ["Strict-Transport-Security","Content-Security-Policy","X-Frame-Options","X-Content-Type-Options","Referrer-Policy","X-XSS-Protection"]

def check_header(domain):
    data = requests.get(domain)

    data_headers= data.headers
    for name in headers_name:
        #for key,value in data_headers.items():
        #    if name == key:
        #        list_checked.append(name)

        if name in data_headers:
            print("[PASS]",name,":",data_headers[name])
            if name == "X-Content-Type-Options" and data_headers.get(name) != "nosniff":
                print(" [WARN] X-Content-Type-Options present but not set to 'nosniff' ")

            if name == "X-Frame-Options" and data_headers.get(name) != "DENY" and data_headers.get(name) != "SAMEORIGIN":
                 print("[WARN] X-Frame-Options has weak value")  
                 
            print("----------------------------------------")
        else:
            print("[FAIL]",name,": UNKOWN SINCE IT DOESNT EXIST")
            print("----------------------------------------")
            


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