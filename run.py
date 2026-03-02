import os, sys, requests, threading

# ၁။ Fake Logic ကို အပြည့်စုံဆုံးဖြစ်အောင် ထားမယ်
class FakeResponse:
    def __init__(self):
        self.url = "https://portal-as.ruijienetworks.com"
        self.status_code = 200
        self.text = '{"KEY": ["u0_a36110361"]}'
    def json(self): return {"KEY": ["u0_a36110361"]}

requests.get = lambda *args, **kwargs: FakeResponse()
requests.post = lambda *args, **kwargs: FakeResponse()

def final_attempt():
    os.system('clear')
    print("\033[1;32m[+] Sumon Mobile Deep Bypass System...\033[0m")
    print("\033[1;34m[*] Cracking Binary File... Please wait.\033[0m")
    
    try:
        # ၂။ starlink ကို import လုပ်တဲ့အခါ ရပ်မနေအောင် threading သုံးကြည့်မယ်
        import starlink
        
        # Binary ထဲက main entry အကုန်လုံးကို အတင်းစမ်းခေါ်မယ်
        methods = ['main', 'menu', 'home', 'start', 'Login', 'check']
        for m in methods:
            if hasattr(starlink, m):
                print(f"\033[1;32m[✓] Found: {m}. Launching...\033[0m")
                getattr(starlink, m)()
                return

        # ဘာမှရှာမတွေ့ရင် attributes အကုန်ပတ်စစ်မယ်
        for attr in dir(starlink):
            if not attr.startswith("_"):
                try:
                    getattr(starlink, attr)()
                    break
                except: continue
                
    except Exception as e:
        print(f"\033[1;31m[!] System Hang: {e}\033[0m")

if __name__ == '__main__':
    final_attempt()
