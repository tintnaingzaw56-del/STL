import starlink
# starlink ထဲက main menu ကို တိုက်ရိုက် ခေါ်ခိုင်းတာပါ
try:
    starlink.main() 
except:
    try:
        starlink.menu()
    except Exception as e:
        print(f"Error: {e}")
