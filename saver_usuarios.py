usuarios = []
trasporte = {}
infousu = {}

def adicionar(add):
    usuarios.append(add)
    print(f'o usuario {infousu["nome"]} foi adicionado')
        
def mostar():
    print(usuarios)
       
def delattr():
    usuarios.pop(0)
    

while True:
    print('----------------------------\n')
    print('adicionar usuario -------->1\n')
    print('mostrar usuario e objeto-->2\n')
    print('deletar usuario ---------->3\n')
    print('sair do programa---------->4\n')
    resp = int(input("Digite uma opção --->"))
    
    match resp:
         case 1:
            infousu["nome"] = input("Digite seu nome de usuario \n")
            infousu["idade"] = int(input("Digite sua idade de usuario \n"))
            infousu["cpf"] = int(input("Digite seu cpf de usuario \n"))
            infousu["cidade"] = input("Digite sua cidade de usuario \n")
            trasporte["tem"]  = int(input("tem trasporte pobre! (1sim/2nao) \n"))
            if trasporte["tem"] == 1:
                trasporte["tipo_trasporte"] = input("qual seu tipo de trasporte \n")
                trasporte["trasporte"] = input("qual é o modelo do seu trasporte \n")
                trasporte["situacao_trasporte"] = input("seu trasporte e pago ou é proprio? \n")
                infousu["trasporte"] = trasporte
            adicionar(infousu)
         case 2:
             mostar()
         case 3:
            
             delattr() 
         case 4:
             print("saindo...\n")
             break
         