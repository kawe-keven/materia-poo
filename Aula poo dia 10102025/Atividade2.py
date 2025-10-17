class Carro:
  """
  Representa um carro que entra na oficina, com seus atributos
  e ações que pode realizar.
  """

  # 1. ATRIBUTOS (definidos no método construtor __init__)
  def __init__(self, marca, modelo, ano):
    """
    Inicializa um novo objeto Carro com suas características.
    """
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    print(f"Novo carro registrado na oficina: {self.marca} {self.modelo} {self.ano}.")

  # 2. MÉTODO (uma ação que o objeto pode fazer)
  def ligar_motor(self):
    """
    Simula a ação de ligar o motor do carro.
    """
    print(f"Ligando o motor do {self.modelo}... Vrum vrum!🚗")


# --- Demonstração de Uso ---

# 3. OBJETO (criação de uma instância da classe)
print("--- Registrando um novo carro ---")
carro_fiat_uno = Carro("Fiat", "Uno", 2010)

# Verificando os atributos do objeto criado
print(f"\nDetalhes do carro:")
print(f"  - Marca: {carro_fiat_uno.marca}")
print(f"  - Modelo: {carro_fiat_uno.modelo}")
print(f"  - Ano: {carro_fiat_uno.ano}")

# 4. CHAMANDO O MÉTODO (executando a ação)
print("\n--- Ação na oficina ---")
carro_fiat_uno.ligar_motor()