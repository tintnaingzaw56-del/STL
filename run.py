import os, sys

# ၁။ မူရင်း Key စစ်တဲ့ function တွေကို လှည့်စားဖို့ (Fake logic)
class FakeResponse:
    def json(self): return {"KEY": ["u0_a36110361"]}
    def status_code(self): return 200

# ၂။ requests.get ကို အလုပ်မလုပ်အောင် တားဆီးမယ်
import requests
requests.get = lambda *args, **kwargs: FakeResponse()

def start_bypass():
    os.system('clear')
    print("\033[1;32m[+] Sumon Mobile Final Bypass Loading...\033[0m")
    
    try:
        # ၃။ starlink ကို အတင်းအကျပ် သွင်းမယ်
        import starlink
        
        # ၄။ Binary ထဲမှာ ပါလေ့ရှိတဲ့ Main Entry Point တွေကို အစဉ်လိုက် စမ်းခေါ်မယ်
        entry_points = ['main', 'menu', 'home', 'start', 'Login']
        
        found = False
        for entry in entry_points:
            if hasattr(starlink, entry):
                print(f"\033[1;34m[*] Launching via {entry}...\033[0m")
                getattr(starlink, entry)()
                found = True
                break
        
        if not found:
            # ဘာမှရှာမတွေ့ရင် starlink ထဲက function အားလုံးကို scan ဖတ်မယ်
            for func in dir(starlink):
                if not func.startswith("__"):
                    print(f"\033[1;33m[*] Trying hidden function: {func}\033[0m")
                    try:
                        getattr(starlink, func)()
                    except:
                        continue
                        
    except Exception as e:
        print(f"\033[1;31m[!] Bypass Error: {e}\033[0m")

if __name__ == '__main__':
    start_bypass()
