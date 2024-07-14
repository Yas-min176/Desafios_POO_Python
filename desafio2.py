class PlanoTelefone:
    # TODO: Crie o método de inicialização (__init__) para inicializar os atributos 'nome' e 'saldo'.
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = float(saldo)  # Convertendo saldo para float
    
    # TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo.
    def verificar_saldo(self):
        if self.__saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

    # TODO: Adicione um método getter para o atributo 'nome'.
    def get_nome(self):
        return self.__nome

class UsuarioTelefone:
    # TODO: Crie o método de inicialização (__init__) para inicializar os atributos 'nome' e 'plano'.
    def __init__(self, nome, plano):
        self.__nome = nome
        self.__plano = plano
    
    # TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo do plano.
    def mensagem_personalizada(self):
        return self.__plano.verificar_saldo()

    # TODO: Crie um método 'verificar_saldo' para retornar o nome do plano e a mensagem personalizada do plano.
    def verificar_saldo(self):
        saldo = self.__plano.verificar_saldo()
        return self.__plano.get_nome(), saldo

    # TODO: Sobrescreva o método __str__ para retornar uma mensagem indicando a criação do usuário.
    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
nome_plano, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)
