import dns.resolver
import sys

selectors = [
    # Google Workspace
    "google", "google2",
    # Microsoft 365
    "selector1", "selector2",
    # General defaults
    "default", "dkim", "mail", "smtp", "k1", "k2", "s1", "s2",
    # SendGrid
    "s1", "s2", "smtpapi",
    # Mailchimp / Mandrill
    "mandrill", "k1", "mte1", "mte2",
    # Zoho (popular in Morocco)
    "zoho",
    # OVH (very common in Morocco/France)
    "ovhex123456-selector1", "ovhex123456-selector2",
    # Mailjet (popular in Europe/France)
    "mailjet",
    # Sendinblue / Brevo (popular in Europe)
    "mail", "sendinblue",
    # Amazon SES
    "ses", "amazonses",
    # Postmark
    "pm", "postmark",
    # Proton Mail
    "protonmail", "protonmail2", "protonmail3",
    # Infomaniak (Swiss, used in Francophone Africa)
    "infomaniak",
    # Ionos / 1&1 (common in Europe)
    "s1-ionos", "s2-ionos",
    # Mimecast
    "mimecast20190104",
    # SparkPost
    "sparkpostmail",
    # Constant Contact
    "ctct1", "ctct2",
    # Hubspot
    "hs1", "hs2",
    # Freshdesk / Freshworks
    "freshdesk",
    # Zendesk
    "zendesk1", "zendesk2",
    # Turbo-SMTP
    "turbo-smtp",
]

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
            
    except:
        print("[FAIL] No TXT records found")
        return       

def Check_dmarc(domain):
    dmarc_found = False
    try:
        records = dns.resolver.resolve("_dmarc."+domain,"TXT")
        for record in records:
            #print(record)
            record = str(record)
            if record.startswith('"v=DMARC1') :
                dmarc_found = True
        if dmarc_found:
            print("[PASS] DMARC record found")
        else:
            print("[FAIL] No DMARC record")
            
    except:
        print("[FAIL] No TXT records found")
        return    
    
def Check_Dkim(domain):
    Dkim_found = False
    for selector in selectors:
        try:
            
            records = dns.resolver.resolve(selector+"._domainkey."+domain,"TXT")
            for record in records:
                #print(record)
                
                if record.startswith('"') :
                    Dkim_found = True
                if Dkim_found:
                    print("[PASS] DKIM record found")
                else:
                    print("[FAIL] No DKIM record")
                   
        except:
            continue

if len(sys.argv) > 1:
    domain = str(sys.argv[1])
    Check_email(domain)
    Check_dmarc(domain)
    Check_Dkim(domain)

else:
    print("Please enter a domain")
    sys.exit(1)    