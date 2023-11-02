# Função para calcular o valor com desconto com base no número de páginas
def calcular_desconto(num_paginas):
    if num_paginas < 10:
        return num_paginas
    elif num_paginas < 100:
        return num_paginas * 0.9
    elif num_paginas < 1000:
        return num_paginas * 0.85
    elif num_paginas < 10000:
        return num_paginas * 0.8
    else:
        return None

# Função para escolher o tipo de serviço
def escolha_servico():
    while True:
        servico = input("Entre com o tipo de serviço desejado:\nDIG - Digitalização\nICO - Impressão Colorida\nIBO - Impressão Preto e Branco\nFOT - Fotocópia\n>>").strip().upper()
        if servico in ["DIG", "ICO", "IBO", "FOT"]:
            return servico
        else:
            print("Escolha Inválida. Entre com o tipo de serviço novamente.")

# Função para escolher o número de páginas com desconto
def escolha_num_paginas():
    while True:
        try:
            num_paginas = int(input("Entre com o número de páginas: "))
            if num_paginas >= 10000:
                print("Não aceitamos tantas páginas de uma vez.")
            else:
                desconto = calcular_desconto(num_paginas)
                if desconto is not None:
                    return desconto
                else:
                    print("Número de páginas fora do intervalo válido.")
        except ValueError:
            print("Por favor, entre com um valor numérico válido.")

# Função para escolher serviço adicional
def servico_extra():
    while True:
        try:
            extra = int(input("Deseja adicionar mais algum serviço?\n1 - Encadernação Simples - R$ 10,00\n2 - Encadernação Capa Dura - R$ 25,00\n0 - Não desejo mais nada\n>>"))
            if extra in [0, 1, 2]:
                return extra
            else:
                print("Escolha Inválida. Entre com uma opção válida.")
        except ValueError:
            print("Por favor, entre com uma opção válida.")

# Função principal
def main():
    # Mensagem de boas-vindas
    print("Bem Vindo ao petshop do Ronaldo Queiroz da Silva")

    # Escolher serviço
    servico = escolha_servico()

    # Escolher número de páginas com desconto
    desconto_paginas = escolha_num_paginas()

    # Escolher serviço adicional
    extra = servico_extra()

    # Dicionário com os preços dos serviços
    precos = {"DIG": 1.10, "ICO": 1.00, "IBO": 0.40, "FOT": 0.20}

    # Calcular o valor total
    total = precos[servico] * desconto_paginas
    if extra == 1:
        total += 10.00
    elif extra == 2:
        total += 25.00

    # Imprimir o resultado
    print(f"Total (R$): {total:.2f} (serviço: {precos[servico]:.2f} páginas: {desconto_paginas:.2f} + extra(s): {10.00 if extra == 1 else 25.00 if extra == 2 else 0.00})")

if __name__ == "__main__":
    main()
