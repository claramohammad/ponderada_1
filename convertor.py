temp = float(input("Coloque a temperatura:"))
unid = input("Unidade (C ou F): ")

if unid.upper() == "C":
    f = 9*temp/5 + 32
    print("A temperatura em F é: ", f)
elif unid.upper() == "F":
    c = 5*(temp-32)/9
    print("A temperatura em C é: ", c)
else:
    print("Unidade de temperatura inválida!")