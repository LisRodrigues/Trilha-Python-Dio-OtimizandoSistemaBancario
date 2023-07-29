def deposito (saldo):
    global  contador_deposito, deposito_dici
    deposito = float(input("Digite o valor deseja depositar: "))
    if (deposito > 0):
        saldo = saldo+deposito
        deposito_dici = deposito_dici +"               "+ (str(contador_deposito)) + "          -     " + (str(deposito)) + "\n"
        contador_deposito = contador_deposito + 1
        
        print("Depósito feito com sucesso!")
    else:
        print("Esse valor não é válido. Por favor, tente novamente.")
    return saldo
    
def saque(saldo):
    global  contador_saque,saque_extrato
    if saldo > 0:
        if contador_saque <= 3:
            saque = float(input("Digite o valor que deseja sacar: "))
            if saque <= 500.0:
                contador_saque = contador_saque + 1
                saldo = saldo - saque
                saque_extrato  = saque_extrato +"               "+ (str(contador_saque)) + "          -    -" + (str(saque)) + "\n"
                
                print("Saque feito com sucesso!")
            else:
                print ("Esse valor exerce o limite de R$ 500,00.")
        else:
            print ("Você já realizou 3 saques hoje, é o limite. Volte outro dia.")
    else:
        print ("Você não possui saldo para realizar essa operação.")
    return saldo

def extrato(saldo_inicial,*,deposito_dici,saque_extrato):
        extrato = f"""
                ********** Extrato **********
            Dépositos:
            {deposito_dici}\n\n
            Saques:
            {saque_extrato}\n\n
            Saldo final: R$ {saldo_inicial}.

                """
        return print(extrato) 

def criar_usuario(lista):
    nome = input("Digite seu nome: ")
    Data_nascimento = input("Digite sua data de nascimento [dd/mm/aa]: ")
    CPF = int(input("Insira seu cpf: "))
    logradouro = input("Insira seu endereço: ")
    numero_casa=int(input("Insira o número da casa: "))
    cidade_es=input("Insira a Cidade/Estado: ")
    new_dici ={"nome":nome,"Data de Nascimento":Data_nascimento,"CPF":CPF,"endereço":{"Logradouro":logradouro,"Número_Casa":numero_casa,"Cidade_es":cidade_es}}
    for user in lista:
        if user["CPF"] == CPF:
            print("Esse CPF já consta no nosso servidor!")
            return

    lista.append(new_dici)
    print("Usuário criado com sucesso!") 
    
def criar_conta(lista, lista_conta):
    global num_conta
    num_agenci ="0001"
    CPF = int(input("Digite seu cpf: "))
    for user in lista:
        if user["CPF"] == CPF:
            num_conta = num_conta+1
            new_dici ={"CPF":CPF,"Número da conta": num_conta,"Número da agência": num_agenci}
            lista_conta.append(new_dici)
            return
        
    print("Esse usuário não conta em nossos registros.") 

saldo_inicial = 1500.65
deposito_dici = "Número do déposito   -    Valor (R$)\n"
saque_extrato = "Número de saque     -    Valor (R$)\n"
contador_deposito = 1 
contador_saque = 1
options =-1
lista =[]
lista_conta =[]
num_conta = 0

while options != 0 :
    options=int(input("Qual seu desejo:\n[1] Depositar\n[2] Sacar\n[3] Extrato\n[4] Cadastrar novo usuário\n[5] Criar conta corrente\n[0] Sair\n"))
    if options == 1:
        saldo_inicial = deposito(saldo_inicial)
    elif options == 2:
        saldo_inicial = saque(saldo_inicial)
    elif options == 3:
        extrato(saldo_inicial, deposito_dici = deposito_dici, saque_extrato=saque_extrato)
    elif options == 4:
        criar_usuario(lista)
    elif options == 5:
        criar_conta(lista,lista_conta)