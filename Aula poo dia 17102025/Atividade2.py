class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "som genérico"
    
    def info(self):
        return f"{self.nome} ({self.__class__.__name__})"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"
    
    def abanar_rabo(self):
        return f"{self.nome} está abanando o rabo!"

class Gato(Animal):
    def falar(self):
        return "Miau!"
    
    def arranhar_moveis(self):
        return f"{self.nome} está arranhando os móveis!"

# Criando lista com animais
animais = [Cachorro("Rex"), Gato("Mimi"), Cachorro("Thor"), Gato("Luna")]

print("=== ZOO VIRTUAL ===\n")

# Percorrendo a lista e chamando métodos
for animal in animais:
    print(f"{animal.info()} faz: {animal.falar()}")
    
    # Métodos específicos de cada classe
    if isinstance(animal, Cachorro):
        print(f"  → {animal.abanar_rabo()}")
    elif isinstance(animal, Gato):
        print(f"  → {animal.arranhar_moveis()}")

print(f"\nTotal de animais: {len(animais)}")
print(f"Cachorros: {len([a for a in animais if isinstance(a, Cachorro)])}")
print(f"Gatos: {len([a for a in animais if isinstance(a, Gato)])}")

# Demonstração adicional
print("\n=== DEMONSTRAÇÃO INDIVIDUAL ===")
rex = Cachorro("Rex")
thor = Cachorro("Thor")
mimi = Gato("Mimi")
luna = Gato ("Luna")

print(f"\n{rex.info()}:")
print(f"  Falar: {rex.falar()}")
print(f"  Ação: {rex.abanar_rabo()}")

print(f"\n{thor.info()}:")
print(f"  Falar: {thor.falar()}")
print(f"  Ação: {thor.abanar_rabo()}")

print(f"\n{mimi.info()}:")
print(f"  Falar: {mimi.falar()}")
print(f"  Ação: {mimi.arranhar_moveis()}")

print(f"\n{luna.info()}:")
print(f"  Falar: {luna.falar()}")
print(f"  Ação: {luna.arranhar_moveis()}")
