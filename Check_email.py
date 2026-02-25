import dns.resolver
import sys


def Check_email(domain):
    spf_found = False
    
    try:
        records = dns.resolver.resolve(domain,"TXT")
        for record in records:
            #print(record)
            record = str(record)
            if record.startswith('"v=spf1') :
                spf_found = True
        if spf_found:
            print("[PASS] SPF record found")
        else:
            print("[FAIL] No SPF record")
            print("you may be in danger to spoofing attacks")
    except:
        print("[FAIL] No TXT records found")
        return       

def check_dmarc(domain):


if len(sys.argv) > 1:
    domain = str(sys.argv[1])
    data = Check_email(domain)

else:
    print("Please enter a domain")
    sys.exit(1)    