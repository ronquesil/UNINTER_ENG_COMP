def calculate_discounted_price():
    # Mensagem de boas-vindas
    print("Bem-vindo à Loja do Ronaldo Queiroz da Silva")

    # Recebe o valor do produto e a quantidade
    product_value = float(input("Entre com o valor do produto: R$ "))
    quantity = int(input("Entre com a quantidade do produto: "))

    # Calcula o valor total sem desconto
    total_value = product_value * quantity

    # Calcula o desconto conforme o valor total
    if total_value < 1000:
        discount = 0
    elif total_value < 3000:
        discount = 0.03
    elif total_value < 5000:
        discount = 0.05
    else:
        discount = 0.08

    # Calcula o valor com desconto
    discounted_value = total_value * (1 - discount)

    # Exibe os resultados
    print(f"O valor SEM desconto: R$ {total_value:.2f}")
    print(f"O valor COM desconto: R$ {discounted_value:.2f}")

# Para testar o programa, vamos chamar a função
calculate_discounted_price()
