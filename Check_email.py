import dns.resolver
import sys


def Check_email(domain):

    spl_found = False

    records = dns.resolver.resolve(domain,"TXT")
    for record in records:
        #print(record)
        record = str(record)
        if record.startswith('"v=spf1') :
            spl_found = True

    if spl_found:
        print("[PASS] SPF record found")
    else:
        print("[FAIL] No SPF record")
        print("you may be in danger dor spooofing attacks")


if len(sys.argv) > 1:
    domain = str(sys.argv[1])
    data = Check_email(domain)

else:
    print("Please enter a domain")
    sys.exit(1)    