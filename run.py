import os, sys, requests

# SSL warning ပိတ်မယ်
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ၁။ Fake Logic ကို ပိုမိုပြည့်စုံအောင် ပြင်ဆင်ခြင်း
class FakeResponse:
    def __init__(self):
        self.url = "https://portal-as.ruijienetworks.com"
        self.status_code = 200
        self.text = '{"KEY": ["u0_a36110361"]}'
    def json(self):
        return {"KEY": ["u0_a36110361"]}

# ၂။ requests.get ကို အပြီးအပိုင် လွှဲပစ်မယ်
requests.get = lambda *args, **kwargs: FakeResponse()
requests.post = lambda *args, **kwargs: FakeResponse()

def final_bypass():
    os.system('clear')
    print("\033[1;32m[+] Sumon Mobile Deep Bypass System...\033[0m")
    
    try:
        # ၃။ starlink ကို တိုက်ရိုက်ခေါ်မယ်
        import starlink
        
        # ၄။ ပုံမှန် Entry points တွေအပြင် အကုန်လုံးကို စမ်းမယ်
        entry_list = ['main', 'menu', 'home', 'start']
        found = False
        
        for method in entry_list:
            if hasattr(starlink, method):
                print(f"\033[1;34m[*] Cracking through {method}...\033[0m")
                getattr(starlink, method)()
                found = True
                break
        
        if not found:
            # တကယ်လို့ ဘာမှမရှိရင် function အားလုံးကို scan ဖတ်ပြီး run မယ်
            for name in dir(starlink):
                if not name.startswith("_"):
                    try:
                        getattr(starlink, name)()
                        break
                    except: continue

    except Exception as e:
        # Error တက်ရင်လည်း logic ကို ကျော်ပြီး run ခိုင်းထားမယ်
        pass

if __name__ == '__main__':
    final_bypass()
