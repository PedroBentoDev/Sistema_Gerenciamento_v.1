print("Sistema de Gerenciamento\n")
print("Bem - vindo ! ao sistema\n")

print("Para continuarmos escolha uma opção válida no menu abaixo\n")

while True:
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Concluir")
    print("4 - Excluir")
    print("0 - Sair")

    try:
        opcao_selecionada = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número inteiro.")
        continue

    match opcao_selecionada:
        case 1:
            print("Cadastrar tarefa")
            break
        case 2:
            print("Listando tarefas ...")
            break 
        case 3 :
            print("Concluindo tarefas ...")
            break 
        case 4 :
            print("Excluindo tarefa.....")
            break
        case _:
            print("Opção inválida.")