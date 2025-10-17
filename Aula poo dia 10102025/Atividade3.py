class Animal:
  """
  Uma classe para representar um animal com nome, tipo e um som característico.
  """
  def __init__(self, nome, tipo):
    """
    Inicializa um novo objeto Animal.

    Args:
      nome (str): O nome do animal (ex: "Rex").
      tipo (str): O tipo do animal (ex: "Cachorro").
    """
    self.nome = nome
    self.tipo = tipo

  def emitir_som(self):
    """
    Imprime um som característico dependendo do tipo do animal.
    """
    if self.tipo.lower() == "cachorro":
      print(f"{self.nome}: Au au!")
    elif self.tipo.lower() == "gato":
      print(f"{self.nome}: Miau!")
    elif self.tipo.lower() == "vaca":
      print(f"{self.nome}: Muuuu!")
    else:
      print(f"{self.nome} ({self.tipo}) faz um som desconhecido.")

# --- Demonstração ---

# 1. Criação dos objetos (instâncias da classe Animal)
cachorro = Animal("Bolinha", "Cachorro")
gato = Animal("Frajola", "Gato")

# 2. Fazendo os animais se comunicarem
print("Os animais começam a se comunicar:")
cachorro.emitir_som()
gato.emitir_som()