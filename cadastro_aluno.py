menu = """
[a] Cadastrar aluno
[b] Calcular Média
[c] Informações do aluno
[d] Sair

=> """

aluno = {}

while True:
    opcao = input(menu).lower()

    if opcao == "a":
        print("Cadastro do aluno")
        aluno["nome"] = input("Digite o nome do aluno: ")
        aluno["idade"] = input("Digite a idade do aluno: ")

        notas = []
        for i in range(4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i+1}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota inválida! Digite um valor entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida! Por favor, digite um número.")

        aluno["notas"] = notas
        print("Cadastro concluído com sucesso!")
        print(aluno)

    elif opcao == "b":
        if "notas" in aluno and aluno["notas"]:
            media = sum(aluno["notas"]) / len(aluno["notas"])
            print(f"A média do aluno é {media:.2f}")
            if media >= 7:
                print("Aluno APROVADO")
            else:
                print("Aluno REPROVADO")
        else:
            print("Nenhuma nota cadastrada. Por favor, cadastre o aluno primeiro.")

    elif opcao == "c":
        if aluno:
            print("Informações do aluno:")
            for chave, valor in aluno.items():
                print(f"{chave.capitalize()}: {valor}")
        else:
            print("Nenhum aluno cadastrado ainda.")

    elif opcao == "d":
        print("Saindo... Até a próxima!")
        break

    else:
        print("Opção não encontrada! Tente novamente.")
