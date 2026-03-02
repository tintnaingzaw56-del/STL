import os, requests, sys

# SSL Error မတက်အောင် warning ပိတ်ထားမယ်
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# သင့်ရဲ့ STL repo က key.json link
YOUR_LINK = "https://raw.githubusercontent.com/tintnaingzaw56-del/STL/main/key.json"

def check_approval():
    os.system('clear')
    print("\033[1;34m[+] Checking Approval from Sumon Mobile...\033[0m")
    try:
        # Script က တောင်းနေတဲ့ ID ပုံစံအတိုင်းယူမယ်
        user_id = os.popen('whoami').read().strip()
        
        # GitHub က JSON ကို ဖတ်မယ် (SSL verify ကျော်ထားတယ်)
        response = requests.get(YOUR_LINK, verify=False).json()
        approved_keys = response.get("KEY", [])
        
        # သင့် ID ဖြစ်တဲ့ u0_a36110361 ပါမပါ စစ်မယ်
        if any(user_id in k for k in approved_keys) or user_id in approved_keys or "u0_a36110361" in approved_keys:
            print(f"\033[1;32m[✓] ID Approved! Welcome.\033[0m")
            return True
        else:
            print(f"\033[1;31m[!] YOUR KEY: {user_id}10361 is NOT Approved.\033[0m")
            print("\033[1;33m[?] Contact Admin (Sumon Mobile) for access.\033[0m")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    if check_approval():
        try:
            # Approval အောင်မှ မူရင်း file ကို run မယ်
            __import__('starlink')
        except Exception as e:
            print(f"Script Error: {e}")
