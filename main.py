
print()
print("UniFECAF | Graduação Tecnológica em Inteligência Artificial e Automação Digital")
print("Autor: Waldir Adilson Évora dos Santos | RA: 263388 ")
print()
print("Projeto Final de Algoritmos e Lógica de Programação")
print("Sistema de controle de qualidade de peças")

# essas listas ficam fora do while porque serão usadas durante toda a execução
pecas_aprovadas = []
pecas_reprovadas = []
caixa_atual = []
caixas_fechadas = []

while True:
    # Mostra o menu
    # print() imprime informações na tela
    print()
    print("=========================")
    print("  CONTROLE DE QUALIDADE")
    print("=========================")
    print()
    print("Menu:")
    print("1 - Cadastrar nova peça")
    print("2 - Listar peças aprovadas/reprovadas")
    print("3 - Remover peça cadastrada")
    print("4 - Listar caixas fechadas")
    print("5 - Gerar relatório final")

    # Pergunta a opção
    # input() - recebe um valor digitado pelo usuário
    print()
    opcao = input("Escolha uma opção: ")

    # Mostra a opção escolhida
    print("Você escolheu a opção:", opcao)

    # Fazer o programa tomar decisões
    # elif permite testar outras condições em sequência
    # float - transforma string em um número que aceita casas decimais
    # .lower() - Transforma as letras de uma string em minúsculas (python é case sensitive)
    print()
    if opcao == "1":
        id_peca = input("Digite o ID da peça: ")
        peso = float(input("Digite o peso da peça em gramas: "))
        cor = input("Digite a cor da peça: ").lower()
        comprimento = float(input("Digite o comprimento da peça em cm: "))

        # Lista - motivos
        # .append() - nos permite adicionar um item ao final da lista
        # len() - verifica quantos itens existem na lista
        motivos = []
        print()

        print("ID informado:", id_peca)
        print("Peso informado:", peso)
        print("Cor informada:", cor)
        print("Comprimento informado:", comprimento)
        print()

        # Verificação do peso - entre 95g e 105g incluindo os próprios valores
        # Uso de operador lógico AND: SE verdadeiro AND verdadeiro = verdadeiro
        if peso >= 95 and peso <= 105:
            print(f"Peso {peso} gramas aprovado.")
        else:
            motivos.append(f"Peso {peso} gramas fora do padrão.")

        # Verificação da cor - azul ou verde
        # Uso de operador lógico OR: SE verdadeiro OR verdadeiro = verdadeiro
        if cor == "azul" or cor == "verde":
            print(f"Cor {cor} aprovada.")
        else:
            motivos.append(f"Cor {cor} fora do padrão.")

        # Verificação do comprimento - entre 10 cm e 20 cm incluindo os próprios valores
        # Uso de operador lógico AND: SE verdadeiro AND verdadeiro = verdadeiro
        if comprimento >= 10 and comprimento <= 20:
            print(f"Comprimento {comprimento} cm aprovado.")
        else:
            motivos.append(f"Comprimento {comprimento} cm fora do padrão.")

        # len() - verifica quantos itens existem na lista de motivos. Se a lista tiver 0 motivos de Reprovação a peça foi Aprovada
        # além de mostrar, também guardamos o resultado APROVADA/REPROVADA
        if len(motivos) == 0:
            situacao = "APROVADA" 
            print("Peça APROVADA.")
        else:
            situacao = "REPROVADA"
            print("Peça REPROVADA.")
            print("Motivos:")

            # percorre cada elemento da lista
            for motivo in motivos:
                print(motivo)

        # o dicionário armazena as informações em pares chave e valor 
        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento,
            "situacao": situacao,
            "motivos": motivos
        }

        # se a peça foi aprovada... coloca o dicionário inteiro na lista de aprovadas. Caso contrário coloca o dicionário inteiro na lista de reprovadas.
        # quando a contagem na lista caixa_atual for 10... a caixa é guardada na lista de caixas_fechadas.
        # caixas_fechadas é uma lista que pode guardar outras listas.
        if situacao == "APROVADA":
            pecas_aprovadas.append(peca)
            caixa_atual.append(peca)

            if len(caixa_atual) == 10:
                caixas_fechadas.append(caixa_atual)
                caixa_atual = []
                print("Caixa completa e fechada.")

        else:
            pecas_reprovadas.append(peca)

    elif opcao == "2":
        print()
        print("PEÇAS APROVADAS:")

        if len(pecas_aprovadas) == 0:
            print("Nenhuma peça aprovada cadastrada.")
            print()
        else:
            for peca in pecas_aprovadas:
                print("ID:", peca["id"])
                print("Peso:", peca["peso"])
                print("Cor:", peca["cor"])
                print("Comprimento:", peca["comprimento"])
                print()

        print("PEÇAS REPROVADAS:")

        if len(pecas_reprovadas) == 0:
            print("Nenhuma peça reprovada cadastrada.")
            print()
        else:
            for peca in pecas_reprovadas:
                print("ID:", peca["id"])
                print("Peso:", peca["peso"])
                print("Cor:", peca["cor"])
                print("Comprimento:", peca["comprimento"])
                print("Motivos:")

                for motivo in peca["motivos"]:
                    print(motivo)

                print()

    elif opcao == "3":
        print()
        id_remover = input("Digite o ID da peça que deseja remover: ")

        # aqui começo dizendo que não encontrei a peça
        peca_encontrada = False

        # in verifica se a peça está dentro da caixa atual
        for peca in pecas_aprovadas:
            if peca["id"] == id_remover:
                pecas_aprovadas.remove(peca)

                if peca in caixa_atual:
                    caixa_atual.remove(peca)
                else:
                    for caixa in caixas_fechadas:
                        if peca in caixa:
                            caixa.remove(peca)
                            break

                peca_encontrada = True
                print("Peça removida com sucesso.")
                break

        if peca_encontrada == False:
            for peca in pecas_reprovadas:
                if peca["id"] == id_remover:
                    pecas_reprovadas.remove(peca)
                    peca_encontrada = True
                    print("Peça removida com sucesso.")
                    break

        if peca_encontrada == False:
            print("Peça não encontrada.")

    elif opcao == "4":
        print()
        print("CAIXAS FECHADAS:")

        if len(caixas_fechadas) == 0:
            print("Nenhuma caixa fechada.")
        else:
            numero_caixa = 1

            for caixa in caixas_fechadas:
                print()
                print("Caixa", numero_caixa)

                for peca in caixa:
                    print("ID:", peca["id"])

                numero_caixa = numero_caixa + 1

    elif opcao == "5":
        print()
        print("RELATÓRIO FINAL")
        print()

        print("Total de peças aprovadas:", len(pecas_aprovadas))
        print("Total de peças reprovadas:", len(pecas_reprovadas))

        # conta as caixas fechadas e também a caixa atual, se estiver em uso
        quantidade_caixas = len(caixas_fechadas)

        if len(caixa_atual) > 0:
            quantidade_caixas = quantidade_caixas + 1

        print("Quantidade de caixas utilizadas:", quantidade_caixas)

        if len(pecas_reprovadas) > 0:
            print()
            print("PEÇAS REPROVADAS E MOTIVOS:")

            for peca in pecas_reprovadas:
                print()
                print("ID:", peca["id"])

                for motivo in peca["motivos"]:
                    print(motivo)

        print()
        break

    else:
        print("Opção inválida.")

print("Programa encerrado.")
print()