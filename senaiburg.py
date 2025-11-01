validação = int(input("Para continuar insira 1, para parar insira 0"))


while validação == 1:

    nome = input("Insira seu nome:")
    plano = input("Qual é o seu plano? ").upper()

    valor = float(input("Qual o valor gasto no mês?"))
    
    if plano == "BRONZE":
        if valor >= 150 and valor < 300:
            print(f"O cliente {nome}, plano {plano}, receberá um desconto de 8% no próximo mês.")
        elif valor >= 300 and valor < 150:
            print(f"O cliente {nome}, plano {plano}, receberá um desconto de 12% no próximo mês.")
        elif valor >= 500 and valor > 50:
            print(f"O cliente {nome}, Bronze, foi promovido a Prata e receberá um desconto de 12% no próximo mês. ")
        elif valor <= 50:
            print(f"O cliente {nome}, Bronze, está com engajamento baixo.")
    elif plano == "PRATA":
        if valor >= 400 and valor < 700:
            print(f"O cliente {nome}, plano {plano}, receberá um desconto de 10% no próximo mês.")
        elif valor >= 700 and valor < 1200:
            print(f"O cliente {nome}, plano {plano}, receberá um desconto de 18% no próximo mês.")
        elif valor >= 1200 and valor > 150:
            print(f"O cliente {nome}, Prata, foi promovido a Ouro e receberá um desconto de 18% no próximo mês.")
        elif valor <= 150:
            print(f"O cliente {nome}, Prata, corre o risco de voltar para bronze.")

    elif plano == "OURO":
        if valor >= 800 and valor < 1200:
            print(f"O cliente {nome}, plano {plano}, receberá um desconto de 15% no próximo mês.")
        elif valor >= 1200 and valor < 2500:
            print(f"O cliente {nome}, plano {plano}, receberá um desconto de 25% no próximo mês.")
        elif valor >= 2500 and valor > 150:
            print(f"O cliente {nome}, Ouro, ganhou Combo Vitalício por 1 mês e receberá um desconto de 25% no próximo mês.")
        elif valor <= 150:
            print(f"O cliente ${nome}, Ouro, corre risco de voltar para Prata.")
    
    validação = int(input("Para continuar insira 1, para parar insira 0"))

while validação == 0:
    break