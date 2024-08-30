def sacar(saldo):
    print("Seu saldo é de:",saldo, "reais deseja fazer algum saque? ")
    quero = int(input("Digite 1 para SIM ou 0 para NÃO: "))

    if quero == 1:
        valor = float(input("Qual valor deseja sacar: ")) 
        if saldo >= valor:  
            saldo_restante = saldo - valor
            print("Valor sacado!") 
            print("Saldo restante: ", saldo_restante)
            return saldo_restante
        else:
            print("Saldo insuficiente!")
            return saldo
    else:
        print("Operação cancelada!")
        return saldo

    
def depositar(saldo):
    depositado = float(input("Deseja depositar algum valor? Digite 1 para SIM ou 0 para NÃO: "))

    if depositado == 1:
        quero2 = float(input("Qual o valor? "))
        saldo_final = saldo + quero2
        print("Valor depositado!")
        print("Seu saldo Final é: ", saldo_final)
        return saldo_final
    else: 
        print("Finalizando operação, seu saldo na conta é de", saldo)
        return saldo

saldo = 500
saldo = sacar(saldo) 
saldo = depositar(saldo)