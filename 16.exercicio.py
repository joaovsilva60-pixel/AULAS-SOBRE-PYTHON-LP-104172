import os
os.system("cls")
nota = float(input("Digite a nota do aluno: "))

while nota < 0 or nota > 10:
    nota = int(input("Nota inválida! Digite uma nota entre 0 e 10: "))

    print("A nota informada foi:", nota)
    
