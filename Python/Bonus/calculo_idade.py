idade = int(input())

if(idade >= 60):
    print("Idoso")
elif(idade >= 18 and idade <= 59):
    print("Adulto")
elif(idade >= 13 and idade <= 17):
    print("Adolescente")
else:
    print("Criança")            