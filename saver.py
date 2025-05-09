tarefas = []            # Lista principal de tarefas
historico = []          # Pilha para desfazer tarefas
fila_execucao = []      # Fila para executar tarefas


def adicionar_tarefa(tarefa): # |usa o metodo 'def' para criar a função 'adicionar_tarefa' com o parametro 'tarefa'|
    tarefas.append(tarefa) # | usa o método 'append' para adicionar o parametro 'tarefa' na lista 'tarefas' |
    historico.append(tarefa) # | usa o método 'append' para adicionar o parametro 'tarefa' na pilha 'historico' |
    fila_execucao.append(tarefa) # | usa o método 'append' para adicionar o parametro 'tarefa' na fila 'fila_execucao' |
    print(f"Tarefa '{tarefa}' adicionada!\n") # | usa o comando 'print' para mostrar ao usuario a frase "tarefa '{tarefa}' adicionada!" com o parametro '{tarefa}' nomeado pelo usuario|

def desfazer_ultima_tarefa(): # |usa o metodo 'def' para criar a função 'desfazer_ultima_tarefa' sem parametros|
    if historico: # |usa o metodo 'if' para verificar se a pilha 'historico' tem algum dado dentro dela |
        ultima = historico.pop() # | define a variavel 'ultima' como "historico.pop", o metodo 'pop' remove o ultimo dado dentro da pilha|
        tarefas.remove(ultima) # | usa o método 'remove' para aplicar a variavel 'ultima' na lista 'tarefas' |
        fila_execucao.remove(ultima) # | usa o método 'remove' para aplicar a variavel 'ultima' na fila 'fila_execucao' |
        print(f"Tarefa '{ultima}' desfeita!\n") # | usa o comando 'print' para mostrar ao usuario a frase "tarefa '{ultima}' desfeita!" com a variavel '{ultima}' que recebe o nome da tarefa que estava na pilha 'historico'|
    else:  # |usa o metodo 'else' para realizar a contrra parte do 'if' da linha 13 |
        print("Nenhuma tarefa para desfazer.\n") # | usa o comando 'print' para mostrar ao usuario a frase "Nenhuma tarefa para desfazer." |

def atender_tarefa(): # |usa o metodo 'def' para criar a função 'atender_tarefa' sem  parametros |
    if fila_execucao: # |usa o metodo 'if' para verificar se a fila 'fila_execucao' tem algum dado dentro dela |
        feita = fila_execucao.pop(0) # | define a variavel 'feita' como "fila_execucao.pop(0)", o metodo 'pop(0)' remove o primeiro dado que entrou na fila |
        tarefas.remove(feita) # | usa o método 'remove' para aplicar a variavel 'feita' na lista 'tarefas' |
        print(f"Tarefa '{feita}' atendida!\n")  # | usa o comando 'print' para mostrar ao usuario a frase "tarefa '{feita}' atendida!" com a variavel '{feita}' que recebe o nome da tarefa que estava na lista 'tarefas'|
    else: # |usa o metodo 'else' para realizar a contrra parte do 'if' da linha 21 |
        print("Nenhuma tarefa para atender.\n") # | usa o comando 'print' para mostrar ao usuario a frase "Nenhuma tarefa para atender." |

def mostrar_tarefas(): # |usa o metodo 'def' para criar a função 'mostrar_tarefa' sem  parametros |
    print("\n📋 Lista de Tarefas:") # | usa o comando 'print' para mostrar ao usuario a frase "📋 Lista de Tarefas:" |
    for i, t in enumerate(tarefas): # | usa o metodo 'for' para criar as variaveis 'i' e 't' e usa 't' para enumerar os dados dentro da lista 'tarefa' |
        print(f"{i + 1}- {t}") # | usa o comando 'print' para mostrar ao usuario a frase "{i + 1}- {t}" onde 'i' é um incremento  e 't' para mostras os dados dentro da lista 'tarefas' |

while True:  # | usa o metodo 'while' definido como true para criar um loop |
    print("|1 ---> Adicionar Tarefa           |") # | usa o comando 'print' para mostrar ao usuario a frase "1. Adicionar Tarefa" |
    print("|2 ---> Desfazer Última Tarefa     |") # | usa o comando 'print' para mostrar ao usuario a frase "2. Desfazer Última Tarefa" |
    print("|3 ---> Atender Tarefa (modo fila) |") # | usa o comando 'print' para mostrar ao usuario a frase "3. Atender Tarefa (modo fila)" |
    print("|4 ---> Mostrar Tarefas            |") # | usa o comando 'print' para mostrar ao usuario a frase "4. Mostrar Tarefas" |
    print("|5 ---> Sair                       |\n") # | usa o comando 'print' para mostrar ao usuario a frase "5. Sair" |

    opcao = input("Escolha uma opção ---->       |") # |denifine uma variavel 'opcao' como 'input("Escolha uma opção: \n")' onde o metodo 'input' solicita ao usuário a digitação de um texto |

    if opcao == '1': # | usa o método 'if' para definir um loop juntamente com o while da linha 33 e verifica se a variável 'opcao' é equivalente a 1 |
        
        tarefa = input("Digite a tarefa: ") # | denifine uma variavel 'tarefa' como 'input(Digite a tarefa: \n)' onde o metodo 'input' solicita ao usuário a digitação de um texto |
        data_de_inicio= input("digite a data atual (dd/mm/aaaa) \n ") # | denifine uma variavel 'data_de_inicio' como 'input("digite a data atual (dd/mm/aaaa) \n")' onde o metodo 'input' solicita ao usuário a digitação de um texto |

        adicionar_tarefa(f'{tarefa} Inicio: ({data_de_inicio})' ) # | usa a função 'adicionar_tarefa' para adicior o elemento '{tarefa} Inicio: ({data_de_inicio}) fim({data_de_conclusao})' na lista 'tarefas' |
    elif opcao == '3': # | usa o metodo 'elif' para verificar se a variavel 'opcao' é equivalente a 3, se for ele realiza um codigo abaixo |
        atender_tarefa() # | é o comando a ser executado pelo 'elif' da linha 48 chama a função 'atender_tarefa' |
    elif opcao == '4': # | usa o metodo 'elif' para verificar se a variavel 'opcao' é equivalente a 4 , se for ele realiza um codigo abaixo |
        mostrar_tarefas() # | é o comando a ser executado pelo 'elif' da linha 50 chama a função 'mostrar_tarefas' |
    elif opcao == '5': # | usa o metodo 'elif' para verificar se a variavel 'opcao' é equivalente a 5 , se for ele realiza um codigo abaixo |
        print("Saindo do programa...\n") # | usa o comando 'print' para mostrar ao usuario a frase "Saindo do programa..." |
        break # | é um comando que termina o loop de repetição |
    else: # | é a contra parte do 'if' da linha 42 |
        print("Opção inválida!\n") # | usa o comando 'print' para mostrar ao usuario a frase "Opção inválida!" |
        
negoco = "nome_do_negoco.txt" # | define uma variavel 'negoco' como arquivo de texto e o nomeia de 'nome_do_negoco.txt' |
if tarefas: # | identifica se a lista 'tarefas' tem agum elemento dentro dela |
    with open(negoco,"w") as file: #o metodo 'open' abre a variavel 'negoco' em modo de texto e coloca 'negoco' como um arquivo |                                                                                                                                                                                          
        for item in tarefas: # | abre uma estrutura condicional onde verifica se a variavel 'iten' esta dentro da lista 'tarefas' |
            file.write(item + "\n") # | usa o metodo 'write' para escrever a variavel 'iten' no arquivo 'negoco'

    print(f'esta salvo em {negoco}!\n') # | usa o comando 'print' para mostrar ao usuario a frase "esta salvo em {negoco}! onde {negoco} e o nome dado a essa variavel" |