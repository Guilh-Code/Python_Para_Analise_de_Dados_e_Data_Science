Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (x * 9/5) + 32, Celsius)
print(list(Fahrenheit))