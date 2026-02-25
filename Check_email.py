import dns.resolver
import sys


def Check_email(domain):

    records = dns.resolver.resolve(domain,"TXT")
    for record in records:
        print(record)
    


if len(sys.argv) > 1:
    domain = str(sys.argv[1])
    data = Check_email(domain)

else:
    print("Please enter a domain")
    sys.exit(1)    