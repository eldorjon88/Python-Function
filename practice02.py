def yosh_hisobla(tugilgan_yil, hozirgi_yil):
    return hozirgi_yil - tugilgan_yil

yil = int(input("Tug'ilgan yilingizni kiriting: "))
hozirgi_yil = 2025

yosh = yosh_hisobla(yil, hozirgi_yil)

print("Sizning yoshingiz:", yosh)
