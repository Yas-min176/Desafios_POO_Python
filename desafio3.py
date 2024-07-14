# Classe que representa um usuário de telefone com métodos para fazer chamadas.
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome  # Atributo encapsulado para armazenar o nome do usuário
        self.__numero = numero  # Atributo encapsulado para armazenar o número de telefone
        self.__plano = plano  # Atributo encapsulado para armazenar o plano telefônico

    # Método para permitir que um usuário faça uma chamada telefônica.
    def fazer_chamada(self, destinatario, duracao):
        custo = self.__plano.custo_chamada(duracao)  # Calcula o custo da chamada usando o método do plano
        if self.__plano.deduzir_saldo(custo):  # Verifica se o saldo do plano é suficiente
            saldo_restante = self.__plano.verificar_saldo()  # Verifica o saldo restante após a chamada
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_restante:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

# Classe que representa o plano de um usuário de telefone.
class Plano:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo encapsulado para armazenar o saldo inicial do plano

    # Método para verificar o saldo atual do plano.
    def verificar_saldo(self):
        return self.__saldo  # Retorna o saldo atual

    # Método para calcular o custo de uma chamada supondo o custo de $0.10 por minuto.
    def custo_chamada(self, duracao):
        return duracao * 0.10  # Custo de $0.10 por minuto

    # Método para deduzir o valor do saldo do plano após uma chamada.
    def deduzir_saldo(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            return True
        else:
            return False

# Classe que representa um usuário pré-pago, herdando de UsuarioTelefone.
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário.
nome = input()
numero = input()
saldo_inicial = float(input())

# Criando um objeto de UsuarioPrePago com os dados fornecidos.
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)

# Recebendo informações da chamada do usuário.
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado.
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
