from fila import FilaSupermercado
from cliente import Cliente

class Menu:
    def menu(self):
        fila = FilaSupermercado()

        while True:
            print("\n===== CAIXA DO SUPERMERCADO =====")
            print("1 - Entrar na fila")
            print("2 - Atender próximo cliente")
            print("3 - Ver fila atual")
            print("4 - Ver quantidade de pessoas na fila")
            print("5 - Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.entrar_na_fila(fila)
            elif opcao == "2":
                self.atender_proximo(fila)
            elif opcao == "3":
                self.ver_fila(fila)
            elif opcao == "4":
                self.ver_quantidade(fila)
            elif opcao == "5":
                print("Encerrando o programa. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def entrar_na_fila(self, fila):
        nome = input("Nome do cliente: ").strip()
        if not Cliente.validar_nome(nome):
            return

        resposta = input("O cliente é preferencial (idoso/gestante ou PCD)? (Sim/Não): ").strip().lower()
        while resposta not in ("sim", "s", "não", "nao", "n"):
            resposta = input("Resposta inválida. Digite Sim ou Não: ").strip().lower()

        eh_preferencial = resposta in ("sim", "s")

        cliente = Cliente(nome, preferencial=eh_preferencial)
        fila.entrar(cliente)
        tipo = "Preferencial" if cliente.preferencial else "Normal"
        print(f"O(A) cliente {cliente} entrou na fila {tipo}.")

    def atender_proximo(self, fila):
        cliente = fila.atender()
        if cliente is None:
            print("Não há clientes para atender.")
        else:
            tipo = "Preferencial" if cliente.preferencial else "Normal"
            print(f"Atendendo cliente {tipo}: {cliente}")

    def ver_fila(self, fila):
        print("\n--- Fila Preferencial ---")
        clientes = fila.listar_preferencial()
        if clientes:
            for posicao, cliente in enumerate(clientes, start=1):
                print(f"{posicao}. {cliente}")
        else:
            print("(Vazia)")

        print("\n--- Fila Normal ---")
        clientes = fila.listar_fila_normal()
        if clientes:
            for posicao, cliente in enumerate(clientes, start=1):
                print(f"{posicao}. {cliente}")
        else:
            print("(Vazia)")

    def ver_quantidade(self, fila):
        print(f"Total de clientes aguardando: {fila.total()}")
        print(f"Fila preferencial: {fila.qtd_preferencial()}")
        print(f"Fila normal: {fila.qtd_fila_normal()}")


