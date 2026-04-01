import requests

def verify_master_access():
    # আপনার অনুমোদিত আইপি (উদাহরণ)
    AUTHORIZED_IP = "YOUR_HOME_IP_HERE" 
    
    try:
        current_ip = requests.get('https://api.ipify.org').text
        if current_ip == AUTHORIZED_IP:
            return True
        else:
            print("🚫 Unauthorized Access Attempt! Locking System...")
            return False
    except:
        return False
      
