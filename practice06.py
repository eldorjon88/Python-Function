raqam = input("Telefon raqamingizni kiriting: ")

if len(raqam) == 9 and raqam.isdigit():
    print("To'g'ri raqam.")
else:
    print("Noto'g'ri raqam.")
