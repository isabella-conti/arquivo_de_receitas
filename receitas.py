import os

def criar_receita():
    nome_receita = input("Digite o nome da receita (ou digite 'voltar' para retornar ao menu principal): ")
    if nome_receita.lower() == 'voltar':
        return
    ingredientes = []
    
    def pedir_ingredientes():
        ingrediente = input()
        if ingrediente.lower() == "fim":
            return ingredientes
        ingredientes.append(ingrediente)
        return pedir_ingredientes()
    
    print("Digite os ingredientes (digite 'fim' para parar)")
    ingredientes = pedir_ingredientes()
    modo_de_preparo = input("Digite o modo de preparo: ")

    with open("receitas.txt", "a") as file:
        file.write("Nome da Receita: {}\n".format(nome_receita))
        file.write("Ingredientes:\n")
        for ingrediente in ingredientes:
            file.write("- {}\n".format(ingrediente))
        file.write("Modo de preparo:\n")
        file.write("{}\n".format(modo_de_preparo))
        file.write("\n")
    print("Receita '{}' criada com sucesso!".format(nome_receita))
    criar_receita()

def listar_receitas():
    if not os.path.exists("receitas.txt"):
        print("Não há receitas cadastradas")
        return
    with open("receitas.txt", "r") as file:
        print(file.read())

def consultar_receita():
    if not os.path.exists("receitas.txt"):
        print("Não há receitas salvas")
        return
    receitas = []
    with open("receitas.txt", "r") as file:
        receita_atual = ""
        for line in file:
            if line.strip() != "":
                receita_atual += line
            else:
                receitas.append(receita_atual)
                receita_atual = ""
        if receita_atual:
            receitas.append(receita_atual)

    print("Receitas disponíveis para consulta:")
    for i, receita in enumerate(receitas, 1):
        print(f"{i}. {receita.splitlines()[0]}")

    escolha = input("Digite o número da receita que deseja consultar (ou digite 'voltar' para retornar ao menu principal): ")
    if escolha.lower() == 'voltar':
        return
    try:
        escolha = int(escolha)
        if 1 <= escolha <= len(receitas):
            print(receitas[escolha - 1])
        else:
            print("Escolha inválida.")
    except ValueError:
        print("Escolha inválida.")

def limpar_arquivo():
    if os.path.exists("receitas.txt"):
        os.remove("receitas.txt")
        print("Arquivos deletados")
    else:
        print("Não há arquivos para deletar")

def main():
    while True:
        print("\n1 – Criar Receita\n2 – Consultar Receita\n3 – Listar Receitas\n4 – Limpar Arquivo\n5 – Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            criar_receita()
        elif opcao == '2':
            consultar_receita()
        elif opcao == '3':
            listar_receitas()
        elif opcao == '4':
            limpar_arquivo()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
