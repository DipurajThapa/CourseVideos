# file: practice/solutions/task7.py
celsius = float(input("Temperature in Celsius? "))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
print(f"{celsius:.1f} C is {fahrenheit:.1f} F")
print(f"{celsius:.1f} C is {kelvin:.2f} K")
