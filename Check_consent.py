import requests
import sys

cookies_consent = ["cookie-consent", "cookie-banner", "cookieConsent", "consent-banner", "gdpr", "cookie-notice", "onetrust", "cookiebot", "didomi", "trustarc", "axeptio", "cookieyes", "tarteaucitron", "cookie-popup", "consent-dialog", "cc-banner"]

def Check_consent(domain):
    found = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}

    data = requests.get(domain,headers=headers)
    html = data.text.lower()
  
    consent = False
    for cookie_consent in cookies_consent:
        if cookie_consent in html:
            consent = True
            found.append(cookie_consent)
    
    if consent:
        print ("[PASS] consent does exist")
        print(found)
    else:
        print(print("[FAIL] No consent banner detected in static HTML (may load via JavaScript)"))
        


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