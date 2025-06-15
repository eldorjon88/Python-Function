def teskari_soz_tekshir():
    palindromlar = ["level", "madam", "radar", "kayak"]
    print("Palindrom so'zlar ro'yxati:", ", ".join(palindromlar))
    
    soz = input("So'z kiriting: ")
    teskari = soz[::-1]
    
    if soz.lower() == teskari.lower():
        print("Bu so'z to'g'ri.✔️")
    else:
        print("Bu so'z to'g'ri emas.")

teskari_soz_tekshir()
