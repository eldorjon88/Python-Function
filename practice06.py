def raqamni_tekshir(raqam):
    if len(raqam) == 9 and raqam.isdigit():
        return "To'g'ri raqam.✔️"
    else:
        return "Noto'g'ri raqam."

raqam = input("Telefon raqamingizni kiriting: ")
natija = raqamni_tekshir(raqam)
print(natija)

