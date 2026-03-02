import os, requests, sys

# SSL Verification Error ကို ကျော်ဖို့
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# သင်အခုသုံးနေတဲ့ STL repo ရဲ့ Raw Link ဖြစ်ရပါမယ်
YOUR_LINK = "https://raw.githubusercontent.com/tintnaingzaw56-del/STL/main/key.json"

def check_approval():
    os.system('clear')
    print("\033[1;34m[+] Checking Approval from Sumon Mobile...\033[0m")
    try:
        # Script က တောင်းနေတဲ့ ID ပုံစံအတိုင်းယူမယ် (u0_a361 + extra digits)
        # အရှေ့က သင်ပြတဲ့ပုံအရ u0_a36110361 ဖြစ်နေလို့ အဲ့ဒါကို key.json မှာ ထည့်ပေးရမှာပါ
        user_id = os.popen('whoami').read().strip()
        
        # သင့် GitHub က JSON ကို ဖတ်မယ်
        response = requests.get(YOUR_LINK, verify=False).json()
        approved_keys = response.get("KEY", [])
        
        # ဒီနေရာမှာ script က တောင်းတဲ့ key အပြည့်အစုံနဲ့ စစ်ဆေးပါမယ်
        # သင်ပြတဲ့ပုံအရ u0_a36110361 ကို key.json ထဲမှာ ထည့်ထားပေးပါ
        if any(user_id in k for k in approved_keys) or user_id in approved_keys:
            print(f"\033[1;32m[✓] ID Approved! Welcome.\033[0m")
            return True
        else:
            print(f"\033[1;31m[!] YOUR KEY: {user_id}10361 is NOT Approved.\033[0m")
            print("\033[1;33m[?] Contact Sumon Mobile for access.\033[0m")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    if check_approval():
        try:
            __import__('starlink')
        except:
            pass
