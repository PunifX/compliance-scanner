import dns.resolver
import sys


def Check_email(domain):

    spl_found = "FALSE"

    records = dns.resolver.resolve(domain,"TXT")
    for record in records:
        #print(record)
        record = str(record)
        if record.startswith('"v=spf1') :
            spl_found = "TRUE"

    if spl_found == "TRUE":
        print("[PASS] SPF record found")
    else:
        print("[FAIL] No SPF record")


if len(sys.argv) > 1:
    domain = str(sys.argv[1])
    data = Check_email(domain)

else:
    print("Please enter a domain")
    sys.exit(1)    