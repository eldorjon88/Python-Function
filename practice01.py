def _hisobla(son1, amal, son2):
    if amal == '+':
        return son1 + son2
    elif amal == '-':
        return son1 - son2
    elif amal == '*':
        return son1 * son2
    elif amal == '/':
        if son2 != 0:
            return son1 / son2
        else:
            return "0 ga bo‘lish mumkin emas!"
    else:
        return "Noto'g'ri amal kiritildi!"

son1 = float(input("Birinchi sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /): ")
son2 = float(input("Ikkinchi sonni kiriting: "))

natija = _hisobla(son1, amal, son2)
print("Natija:", natija)

