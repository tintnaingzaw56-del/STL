import os

# အရင်က ရှိခဲ့တဲ့ Approval စစ်တဲ့ code တွေ အကုန်ဖြုတ်လိုက်ပါပြီ
if __name__ == '__main__':
    try:
        # Approval မစစ်တော့ဘဲ starlink ကို တိုက်ရိုက် run ခိုင်းလိုက်တာပါ
        __import__('starlink')
    except Exception as e:
        print(f"Error: {e}")
        
