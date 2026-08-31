segundos = 3665

horas = segundos // 3600
print(horas)

minutos = (segundos % 3600) // 60
print(minutos)

segundos = (segundos % 3600) % 60
print(segundos)