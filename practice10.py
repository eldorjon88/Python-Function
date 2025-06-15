def parolni_tekshir():
    parol = input("Parolni kiriting: ")
    if len(parol) >= 8:
        print("Parol to'g'ri.✔️")
    else:
        print("Parolni uzaytiring.")

parolni_tekshir()
