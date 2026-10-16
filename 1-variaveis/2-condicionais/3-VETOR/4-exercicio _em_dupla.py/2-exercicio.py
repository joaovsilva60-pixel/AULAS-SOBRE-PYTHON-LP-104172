import os
os.system("cls")

temperaturas = []

for i in range(7):
    temperatura = float(input("Digite a temperatura do dia: "))
    temperaturas.append(temperatura)

print("\nTemperaturas da semana:")
for temperatura in temperaturas:
    print(temperatura, "°C")

media = sum(temperaturas) / 7
maior = max(temperaturas)
menor = min(temperaturas)

print("\nMédia da semana:", round(media, 2), "°C")
print("Maior temperatura:", maior, "°C")
print("Menor temperatura:", menor, "°C")
