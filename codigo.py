usuarios = []
trasporte = {}
infousu = {}

def adicionar(add):
    usuarios.append(add)
    print(f'o usuario {add} foi adicionado')
        
def mostar():
    i = int = 1
    if usuarios:
         print(f'aqui estao os usuarios {usuarios}')
    else:
       print('não existe usuarios')
       
def delattr():
    usuarios.pop
    print(f'{add} foi deletado')
    add.pop
    

while True:
    print('adicionar usuario --->1\n')
    print('mostrar usuario --->2\n')
    print('deletar usuario --->3\n')
    print('sair do programa usuario --->5\n')
    print('------------------>')
    resp =  int(input("Digite uma opção!"))
    
    print(usuarios)
    match resp:
         case 1:
             add = str(input("Digite seu nome"))
             adicionar(add)
         case 2:
             mostar()
         case 3:
            
             delattr() 
         case 4:
             print("saindo...")
             break
         