while True:
    idade = int(input("Informe a idade: "))
    if 0 <= idade <= 120:
        break
    print("Idade fora do range, tente novamente.")

print(f"Idade correta registrada: {idade}\n")