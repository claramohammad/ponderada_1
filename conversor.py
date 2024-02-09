#Pede a temperatura e a unidade de medida 
temp = float(input("Coloque a temperatura:"))
unid = input("Unidade (C ou F): ")

#verifica se a unidade é C ou F e faz a conversão
if unid.upper() == "C":
    f = 9*temp/5 + 32
    print("A temperatura em F é: ", f)

#verifica se a unidade é C ou F e faz a conversão
elif unid.upper() == "F":
    c = 5*(temp-32)/9
    print("A temperatura em C é: ", c)

#caso a unidade não seja C ou F emite uma mensagem de erro
else:
    print("Unidade de temperatura inválida!")