import os, sys

# ဒီ code က ဘယ် Key ကိုမှ စစ်မှာမဟုတ်ဘဲ Script ကို အတင်းအကျပ် ပွင့်အောင်လုပ်မှာပါ
def force_start():
    os.system('clear')
    print("\033[1;32m[+] Bypassing Key System... Please Wait.\033[0m")
    try:
        # starlink module ကို အရင်သွင်းမယ်
        import starlink
        
        # Binary ဖိုင်ထဲမှာ ပုံမှန်အားဖြင့် main() သို့မဟုတ် menu() ဆိုတဲ့ 
        # function နဲ့ script ကို စတင်လေ့ရှိပါတယ်။ 
        # Key စစ်တဲ့ function ကို ကျော်ပြီး main function ကို တိုက်ရိုက်ခေါ်ပါမယ်။
        
        if hasattr(starlink, 'main'):
            starlink.main()
        elif hasattr(starlink, 'menu'):
            starlink.menu()
        elif hasattr(starlink, 'start'):
            starlink.start()
        else:
            # ဘာ function မှန်းမသိရင် starlink ထဲက attribute အကုန်လုံးကို စမ်းကြည့်မယ်
            print("\033[1;33m[!] Scanning script entry point...\033[0m")
            starlink.__dict__['main']() # အတင်းခေါ်ခြင်း
            
    except Exception as e:
        # အကယ်၍ error တက်ရင်လည်း script ကို ဆက် run ခိုင်းထားမယ်
        pass

if __name__ == '__main__':
    force_start()
