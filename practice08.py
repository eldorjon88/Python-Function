def c_to_f(celsius):
    """Celsiusni Fahrenheitga aylantiradi."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def f_to_c(fahrenheit):
    """Fahrenheitni Celsiusga aylantiradi."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

c = 25
f = c_to_f(c)
print(f"{c}°C = {f}°F")

f = 77
c = f_to_c(f)
print(f"{f}°F = {c}°C")
