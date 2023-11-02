# Dicionário com os preços dos sabores e tamanhos
precos = {
    'CP': {'P': 10, 'M': 15, 'G': 19},
    'AC': {'P': 12, 'M': 17, 'G': 21}
}

# Exigência de Código 1 de 8: Mensagem de boas-vindas com o seu nome
print("Bem-vindo à Loja de Gelados do Ronaldo Queiroz da Silva")
print("Cardápio".center(56, "-"))

# Tabela de preços com linhas verticais nas colunas
print("{:<10}| {:<15}| {:<15}".format("Tamanho", "Cupuaçu (CP)", "Açaí (AC)"))
print("-" * 56)
print("{:<10}| R$ {:<12}| R$ {:<12}".format("P", precos['CP']['P'], precos['AC']['P']))
print("{:<10}| R$ {:<12}| R$ {:<12}".format("M", precos['CP']['M'], precos['AC']['M']))
print("{:<10}| R$ {:<12}| R$ {:<12}".format("G", precos['CP']['G'], precos['AC']['G']))
print("-" * 56)

# Inicializando o acumulador
total = 0

# Exigência de Código 7 de 8: Estrutura de loop while
while True:
    # Exigência de Código 2 de 8: Input do sabor com verificação
    sabor = input("Entre com o sabor desejado (CP/AC): ")
    if sabor not in ['CP', 'AC']:
        # Exigência de Saída de Console 2 de 4: Pedido com sabor inválido
        print("Sabor Inválido. Tente novamente.")
        continue

    # Exigência de Código 3 de 8: Input do tamanho com verificação
    tamanho = input("Entre com o tamanho desejado (P/M/G): ")
    if tamanho not in ['P', 'M', 'G']:
        # Exigência de Saída de Console 3 de 4: Pedido com tamanho inválido
        print("Tamanho inválido. Tente novamente.")
        continue

    # Exigência de Código 4 de 8: Calcular preço com base no sabor e tamanho
    preco = precos[sabor][tamanho]
    total += preco

    # Exigência de Saída de Console 4 de 4: Pedido com sabor e tamanho
    print(f"Você pediu {sabor} no tamanho {tamanho}: R$ {preco:.2f}")

    # Exigência de Código 6 de 8: Perguntar se deseja pedir mais alguma coisa
    mais_pedidos = input("Deseja pedir mais alguma coisa (s/digite outra tecla)?: ")
    if mais_pedidos.lower() != 's':
        break

# Exigência de Saída de Console 1 de 4: Mostrar o valor total
print(f"O valor total a ser pago: R${total:.2f}")