A = "Joe"


class Cliente:
    Nome: str
    Renda: float


if __name__ == '__main__':
    A = Cliente()
    B = Cliente()
    A.Nome = "Joe"
    A.Renda = 10000.00
    B.Nome = "Bernard"
    B.Renda = 5000.00

    lista_clientes = [A, B]

    for cliente in lista_clientes:
        if cliente.Renda > 5000.00:
            print("Cliente VIP --> Nome: " + cliente.Nome + ", renda: " + str(cliente.Renda))
        else:
            print("Cliente Normal --> Nome: " + cliente.Nome + ", renda: " + str(cliente.Renda))

