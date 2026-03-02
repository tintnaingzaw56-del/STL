import os, requests, sys

# SSL warning ပိတ်မယ်
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# သင့်ရဲ့ GitHub Key Link
YOUR_KEY_LINK = "https://raw.githubusercontent.com/tintnaingzaw56-del/STL/main/key.json"

def bypass_and_run():
    os.system('clear')
    print("\033[1;34m[+] Sumon Mobile Final Bypass System...\033[0m")
    
    try:
        # ၁။ သင့်ရဲ့ ID ကို GitHub ကနေ အရင်စစ်မယ်
        user_id = os.popen('whoami').read().strip()
        full_key = f"{user_id}10361"
        
        res = requests.get(YOUR_KEY_LINK, verify=False).json()
        if full_key not in res.get("KEY", []):
            print(f"\033[1;31m[!] KEY: {full_key} is not approved.\033[0m")
            return

        print("\033[1;32m[✓] Approval Success! Starting Starlink...\033[0m")
        
        # ၂။ starlink ကို import လုပ်တဲ့အခါ 
        # သူ့အထဲက link တွေကို သင့်ဆီက data နဲ့ အစားထိုးဖို့ ကြိုးစားမယ်
        import starlink
        
        # ဒီနေရာမှာ starlink ရဲ့ function တွေကို တိုက်ရိုက်ခေါ်ကြည့်ပါမယ်
        # strings ထဲမှာ တွေ့တဲ့ link တွေကို ကျော်သွားဖို့ ကြိုးစားတာပါ
        if hasattr(starlink, 'main'):
            starlink.main()
        elif hasattr(starlink, 'menu'):
            starlink.menu()
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    bypass_and_run()
