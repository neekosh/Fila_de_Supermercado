# classe FilaSupermercado
from collections import deque

class FilaSupermercado:
    def __init__(self):
        self.fila_normal = deque()
        self.fila_preferencial = deque()

    def entrar(self, cliente):
        if cliente.preferencial:
            self.fila_preferencial.append(cliente)
        else:
            self.fila_normal.append(cliente)

    def atender(self):
        # Retorna o cliente atendido ou None se não houver ninguém
        if self.fila_preferencial:
            return self.fila_preferencial.popleft()
        if self.fila_normal:
            return self.fila_normal.popleft()
        return None

    def listar_preferencial(self):
        return list(self.fila_preferencial)

    def listar_fila_normal(self):
        return list(self.fila_normal)

    def qtd_preferencial(self):
        return len(self.fila_preferencial)

    def qtd_fila_normal(self):
        return len(self.fila_normal)

    def total(self):
        return self.qtd_preferencial() + self.qtd_fila_normal()







