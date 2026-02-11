tarefas = []

def adicionar_tarefa(trabalhar ):
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!\n")

def listar_tarefas(acordar ,fazerbarba,vestir):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
    else:
        print("\n=== Lista de Tarefas ===")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
        print()

def remover_tarefa():
    listar_tarefas()
    try:
        numero = int(input("Digite o número da tarefa para remover: "))
        if 1 <= numero <= len(tarefas):
            tarefas.pop(numero - 1)
            print("Tarefa removida com sucesso!\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Digite um número válido.\n")

def menu():
    while True:
        print("=== GERENCIADOR DE TAREFAS ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida.\n")

menu()
