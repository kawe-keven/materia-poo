class Aluno:
    """
    Representa um aluno com nome e idade.
    """
    def __init__(self, nome, idade):
        """
        Construtor da classe Aluno.
        Inicializa os atributos nome e idade.
        """
        self.nome = nome
        self.idade = idade

    def estudar(self):
        """
        Método que simula a ação de estudar.
        """
        print(f"{self.nome} está focado em seus estudos.")

    def apresentar(self):
        """
        Método que apresenta o aluno.
        """
        print(f"Olá! Meu nome é {self.nome} e eu tenho {self.idade} anos.")

#Criação e uso do objeto

# 1. Criar um objeto da classe Aluno (aluno1)
aluno1 = Aluno(nome="Maria", idade=20)

# 2. Chamar os métodos do objeto aluno1
aluno1.apresentar()
aluno1.estudar()