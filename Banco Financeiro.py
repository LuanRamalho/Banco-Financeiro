class Bank():
    def cliente():          
        print("Digite a sua agência: ")
        ag = int(input())
        while(ag<1000 or ag>9999):
            print("Agência errada. Por favor, digite a agência correta: ")
            ag = int(input())
        
        print("")
        
        print("Digite a sua conta: ")
        num_conta = int(input())
        while(num_conta<10000 or num_conta>99999):
            print("Conta errada. Por favor, digite a conta correta: ")
            num_conta = int(input())
        
        print("Digite o saldo atual da sua conta: ")
        conta_p = float(input())
     
        print("Pressione qualquer tecla para acessar o menu: ")
        menu = input()
        
        print("")
        print("")
        
        while(menu!="§"):
            print("Digite 1 para verificar o seu saldo:")
            print("Digite 2 para realizar depósito:")
            print("Digite 3 para realizar pagamento:")
            print("Digite 4 para realizar transferência:")
            
            print("")
            print("")
            
            op = int(input())
            if(op==1):
                print("Seu saldo atual é: R$%.2f" % conta_p)
                break
            
            if(op==2):
                print("Digite o valor do depósito a ser realizado: ")
                dep = float(input())
                conta_p = conta_p + dep
                print("Valor da conta atual: R$%.2f" % conta_p)
                break
            
            if(op==3):
                print("Digite o valor da conta a ser pago: ")
                imp = float(input())
                conta_p = conta_p - imp
                while(conta_p<0):
                    print("Você não tem dinheiro suficiente para pagar o determinado imposto")
                
                print("Valor da conta atual: R$%.2f" % conta_p)
                break
            
            if(op==4):
                conta_c = 0.00
                print("Digite a quantia que deseja transferir: ")
                t = float(input())
                conta_p = conta_p - t
                conta_c = conta_c + t
                print("Valor da conta atual: R$%.2f" % conta_p)
                print("Valor da conta do transferido: R$%.2f" % conta_c)
                break

b = Bank
b.cliente()            
                
       
        
        
        
            

