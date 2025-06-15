def baho_aniqla(ball):
    if ball >= 90:
        return "A"
    elif ball >= 80:
        return "B"
    elif ball >= 70:
        return "C"
    else:
        return "F"

ball = int(input("Ball kiriting: "))
natija = baho_aniqla(ball)
print(natija)
