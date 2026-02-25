import sys
import requests

tracking_cookies = [
    # Google Analytics
    "_ga", "_gid", "_gat", "_gat_gtag", "__utma", "__utmb", "__utmc", "__utmz", "__utmv", "_ga_",
    # Facebook / Meta
    "_fbp", "_fbc", "fr", "datr", "sb", "wd",
    # Google Ads
    "_gcl_au", "_gcl_aw", "_gcl_dc", "IDE", "DSID", "test_cookie",
    # Hotjar
    "_hjid", "_hjSession", "_hjSessionUser", "_hjAbsoluteSessionInProgress", "_hjFirstSeen",
    # HubSpot
    "__hstc", "hubspotutk", "__hssc", "__hssrc",
    # Microsoft / Bing
    "_uetsid", "_uetvid", "MUID", "_clck", "_clsk",
    # Discord
    "__dcfduid", "__sdcfduid", "__cfruid",
    # TikTok
    "_ttp", "_tt_enable_cookie",
    # Snapchat
    "_scid", "_sctr",
    # LinkedIn
    "bcookie", "li_sugr", "lidc", "UserMatchHistory", "AnalyticsSyncHistory",
    # Twitter / X
    "guest_id", "personalization_id", "muc_ads",
    # Criteo (common in Morocco/Europe e-commerce)
    "cto_bundle", "cto_bidid", "cto_optout",
    # Matomo / Piwik (popular in Europe for GDPR-friendly analytics)
    "_pk_id", "_pk_ses", "_pk_ref",
    # Adobe Analytics
    "s_cc", "s_sq", "s_vi", "AMCV_",
    # Yandex (some Moroccan sites use it)
    "_ym_uid", "_ym_d", "_ym_isad",
    # General tracking
    "mp_", "ajs_anonymous_id", "ajs_user_id", "__gads", "__gpi",
]


def Check_Cookies(domain):
    cookie_detected = False
    data = requests.get(domain)
    for cookie in data.cookies:
 

        if cookie.name in tracking_cookies:
            print("[FAIL] Tracking cookie set before consent")
            print(cookie.name)
            print("-------------------------------")
            cookie_detected = True
         
    if not cookie_detected :
        print("no tracking cookies detected")
        

if len(sys.argv) > 1:
    domain = str(sys.argv[1])
    if not domain.startswith("https://") and not domain.startswith("http://"):
        domain = "http://" + domain
        Check_Cookies(domain)
    else:
        Check_Cookies(domain)
else:
    print("Please enter a domain")
    sys.exit(1)    