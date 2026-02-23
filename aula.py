'''age = int(input("digite sua idade "))
if age < 18:
    print(f"voce precisa ter mais {18 - age} anos para dirigir")
else:  
     print("voce ja esta aptor a dirigir")'''
"""num_1 = float(input("digite um numero "))
operação = input("operção ")
num_2 = float(input("digite mais um numero "))    


result = None
# estudo função
def calculador(num_1, operação , num_2):
 

    if operação == "+":
        result = num_1 + num_2
        print(result)
    elif operação =="-":
        result = num_1 - num_2
        print(result) 
    elif operação =="*":
        result = num_1 * num_2
        print(result)
    elif operação == "/":
        if num_2 != 0:
            result = num_1 / num_2
            print(result)
        else: print("não é possivel dividir por 0")
    else:print("digite um operador valido +,-,*,/")


calculador(num_1,operação,num_2)"""

#calculador imc

peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))
imc = None

def calc_imc(peso,altura):
    imc = peso/altura**2
    
    if imc < 18.5:
        print(f"seu imc é {imc} voce esta abaixo do peso")
    elif   18.5 <= imc < 25:
        print(f"seu imc é {imc} voce esta com peso normal continue assim")
    elif   25.0 <= imc < 30:
        print(f"seu imc é {imc} voce esta com sobrepeso") 
    elif   30 <= imc < 40:
        print(f"seu imc é {imc} voce esta com obesidade")
    elif imc >= 40:
        print(f"seu imc é {imc} voce esta com obesidade morbida procure um medico")

calc_imc(peso,altura)

