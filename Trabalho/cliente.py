# classe cliente
# classe Cliente
class Cliente:
    def __init__(self, nome, preferencial=False):
        self.nome = nome
        self.preferencial = preferencial

    def __str__(self):
        return self.nome

    @staticmethod
    def validar_nome(nome):
        if not nome or not nome.strip():
            print("O nome não pode ser vazio.")
            return False
        if not nome.replace(" ", "").isalpha():
            print("Digite um nome válido (apenas letras).")
            return False
        return True