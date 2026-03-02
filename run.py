import os, sys, json

# ၁။ လိုအပ်တဲ့ library တွေကို အတင်းသွင်းမယ်
try:
    import requests
except:
    os.system('pip install requests urllib3')
    import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ၂။ Fake Response ဖန်တီးပြီး requests ကို လှည့်စားမယ်
class MockResponse:
    def __init__(self):
        self.status_code = 200
        self.url = "https://portal-as.ruijienetworks.com"
        self.text = '{"KEY": ["u0_a36110361"]}' # သင့် ID ကို ဒီမှာ အသေထည့်ထားတယ်
    def json(self):
        return {"KEY": ["u0_a36110361"]}

# requests ရဲ့ get နဲ့ post function တွေကို fake နဲ့ အစားထိုးမယ်
requests.get = lambda *args, **kwargs: MockResponse()
requests.post = lambda *args, **kwargs: MockResponse()

def start_sumon_mobile():
    os.system('clear')
    print("\033[1;32m[+] Sumon Mobile Ultimate Bypass System...\033[0m")
    print("\033[1;34m[*] Redirecting Server Check to Local...\033[0m")
    
    try:
        # ၃။ starlink ကို သွင်းပြီး run မယ်
        import starlink
        
        # entry points တွေကို ရှာဖွေမယ်
        for entry in ['main', 'menu', 'start', 'Login']:
            if hasattr(starlink, entry):
                getattr(starlink, entry)()
                return
        
        # ဘာမှမရှိရင် function အကုန်လုံးကို အစဉ်လိုက် စမ်းကြည့်မယ်
        for attr in dir(starlink):
            if not attr.startswith("_"):
                try:
                    getattr(starlink, attr)()
                    break
                except: continue
                
    except Exception as e:
        print(f"\033[1;31m[!] Bypass Active but Script Error: {e}\033[0m")

if __name__ == '__main__':
    start_sumon_mobile()
