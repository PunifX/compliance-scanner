import requests
import sys
     

def check_url(domain):

    data = requests.get(domain)

    if data.status_code == 200:
        print("\n","Status: 200 OK")
        
        
    elif data.status_code == 301:
        print("\n","Status: 301 Redirect permenantly (good)")
       
        
    elif data.status_code == 302:
        print("\n","Status: 302 Redirect temporary (bad follow the standard)")
      
        
    else:   
        print(data,"\n","Error try again")

    return data.url
    

def check_https(data_url,domain):
    
    if data_url.startswith("https://"):

        print("Requested: ",domain )
        print("Final URL: ",data_url)
        print("[PASS] Site does redirect HTTP to HTTPS")

    else:
        print("Requested: ",domain)
        print("Final URL: ",data_url)
        print("[FAIL] Site does not redirect HTTP to HTTPS") 

def check_ssl(data_url,domain):

    domain = domain.replace("http://", "https://")

    try:
        test = requests.get(domain)
        print("SSL PASSED")
                
    except requests.exceptions.SSLError:
        print("SSL FAILED")
  

 
    
if len(sys.argv) > 1 and len(sys.argv) < 1:
    domain = str(sys.argv[1])
    if not domain.startswith("https://") and not domain.startswith("http://"):
        domain = "http://" + domain
        
        data_url = check_url(domain)
        check_https(data_url,domain)
        check_ssl(data_url,domain)
    else:
        data_url = check_url(domain)
        check_https(data_url,domain)
        check_ssl(data_url,domain)
else:
    print("Please enter a domain")
    sys.exit(1)    