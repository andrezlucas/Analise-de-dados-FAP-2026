nome = input ("Nome do aluno")
nota1 = float (input("Digite a primeira nota"))
nota2 = float (input("Digite a segunda nota"))
if nota1 >= 7 and nota2 >=7:
    print(f"{nome} está aprovado com as notas {nota1} e {nota2}")
elif nota1 >=7 or nota2 >=7:
   print(f"{nome} esta de recuperação com as notas {nota1} e {nota2}.")
else: print (f"{nome} foi reprovado com a notas {nota1} e {nota2}." ) 