import os, requests, sys

# SSL Error မတက်အောင် Warning ပိတ်မယ်
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# သင့်ရဲ့ Key စာရင်းရှိတဲ့ link
YOUR_LINK = "https://raw.githubusercontent.com/tintnaingzaw56-del/STL/main/key.json"

def check_approval():
    os.system('clear')
    print("\033[1;34m[+] Sumon Mobile Approval System...\033[0m")
    try:
        # Script ကတောင်းတဲ့ YOUR KEY (u0_a36110361) ကို ယူမယ်
        user_id = os.popen('whoami').read().strip()
        full_key = f"{user_id}10361" 

        # GitHub က key.json ကို ဖတ်မယ်
        response = requests.get(YOUR_LINK, verify=False).json()
        approved_keys = response.get("KEY", [])
        
        if full_key in approved_keys or user_id in approved_keys:
            print(f"\033[1;32m[✓] ID: {full_key} Approved!\033[0m")
            return True
        else:
            print(f"\033[1;31m[!] YOUR KEY: {full_key} is NOT Approved.\033[0m")
            print("\033[1;33m[?] Contact Sumon Mobile for Access.\033[0m")
            return False
    except Exception as e:
        print(f"\033[1;31m[!] Server Error: {e}\033[0m")
        return False

if __name__ == '__main__':
    if check_approval():
        # Approval အောင်ရင် မူရင်း script (starlink) ကို တန်း run ခိုင်းမယ်
        # ဒါဆိုရင် မူရင်း server ဆီ သွားစစ်တာကို ကျော်သွားပါလိမ့်မယ်
        try:
            __import__('starlink')
        except:
            pass
