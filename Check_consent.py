import requests
import sys
from bs4 import BeautifulSoup
cookies_consent = ["cookie","cookie-consent", "cookie-banner","cookieConsent", "consent-banner", "gdpr", "cookie-notice"]
def Check_consent(domain):
    data = requests.get(domain)
    html = data.text.lower()
  
    consent = False
    for cookie_consent in cookies_consent:
        if cookie_consent in html:
            consent = True
    
    if consent:
        print("[PASS] consent does exist")
    else:
        print("[FAIL] consent does not exist")
        


if len(sys.argv) > 1:
    domain = str(sys.argv[1])
    if not domain.startswith("https://") and not domain.startswith("http://"):
        domain = "http://" + domain
        Check_consent(domain)
    else:
        Check_consent(domain)
else:
    print("Please enter a domain")
    sys.exit(1)    