son1 = float(input("Birinchi sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /): ")
son2 = float(input("Ikkinchi sonni kiriting: "))


if amal == '+':
    natija = son1 + son2
elif amal == '-':
    natija = son1 - son2
elif amal == '*':
    natija = son1 * son2
elif amal == '/':
    if son2 != 0:
        natija = son1 / son2
else:
    natija = "Noto'g'ri amal kiritildi!"


print("Natija:", natija)
