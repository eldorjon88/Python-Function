def calculate_bmi(weight: float, height: float) -> float:
    if height <= 0:
        raise ValueError("Bo'y 0 dan katta bo'lishi kerak!")
    bmi = weight / (height ** 2)
    return bmi

def bmi_status(bmi: float) -> str:
    if bmi < 18.5:
        return "ozg'inlik"
    elif 18.5 <= bmi < 25:
        return "normal"
    elif 25 <= bmi < 30:
        return "ortiqcha vazn"
    else:
        return "semizlik"

try:
    ogirlik = float(input("Og'irlikni kiriting (kg): "))
    boy_sm = float(input("Bo'yingizni kiriting (sm): "))
    boy = boy_sm / 100 
    
    if boy <= 0:
        print("Bo'y 0 dan katta bo'lishi kerak!")
    else:
        bmi = calculate_bmi(ogirlik, boy)
        holat = bmi_status(bmi)
        print(f"Sizning BMI: {bmi:.2f}")
        print(f"Sizning holatingiz: {holat}")
except ValueError:
    print("Iltimos, to'g'ri raqam kiriting!")
