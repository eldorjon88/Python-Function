soz = input("So'z kiriting: ")

teskari = soz[::-1]

if soz.lower() == teskari.lower():
    print("Bu so'z to'g'ri.✔️")
else:
    print("Bu so'z to'g'ri emas.")
