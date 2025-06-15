def tekshir(taxmin, sirli_son):
    if taxmin == sirli_son:
        return "To'g'ri topdingiz!✔️"
    else:
        return "Xato."

sirli_son = 7
taxmin = int(input("Sirli sonni toping (1-10): "))
natija = tekshir(taxmin, sirli_son)
print(natija)

