contatos = []

for i in range(3):
    print(f"\nCadastro do contato {i + 1}")

    nome = input("Digite o nome completo: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos.append(contato)

print("\n===== LISTA DE CONTATOS CADASTRADOS =====")

for contato in contatos:
    print("\nNome:", contato["nome"])
    print("Telefone:", contato["telefone"])
    print("E-mail:", contato["email"])