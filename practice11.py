def maosh_hisobla():
    maosh = float(input("Maoshingizni kiriting: "))
    soliq_foiz = 15
    soliq = maosh * soliq_foiz / 100
    toza_maosh = maosh - soliq
    print("Soliq miqdori:", soliq)
    print("Soliqdan keyingi maosh:", toza_maosh)

maosh_hisobla()
