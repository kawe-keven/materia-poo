class No:
    def __init__(self, pagina):
        self.pagina = pagina
        self.anterior = None
        self.proximo = None

class HistoricoNavegacao:
    def __init__(self, limite=50):
        self.atual = None
        self.inicio = None
        self.limite = limite
        self.contador = 0

    def visitar(self, pagina):
        novo = No(pagina)
        
        # Se exceder o limite, remove a página mais antiga
        if self.contador >= self.limite:
            self._remover_mais_antigo()
        
        if self.atual:
            # Remove referências futuras ao adicionar nova página
            self.atual.proximo = None
            self.atual.proximo = novo
            novo.anterior = self.atual
        else:
            self.inicio = novo
        
        self.atual = novo
        self.contador += 1
        print(f"🌐 Visitando: {pagina}")

    def _remover_mais_antigo(self):
        if self.inicio:
            proximo = self.inicio.proximo
            if proximo:
                proximo.anterior = None
            self.inicio = proximo
            self.contador -= 1

    def voltar(self):
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            print(f"↩️ Voltando para: {self.atual.pagina}")
            return True
        else:
            print("🚫 Não há página anterior.")
            return False

    def avancar(self):
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            print(f"↪️ Avançando para: {self.atual.pagina}")
            return True
        else:
            print("🚫 Não há próxima página.")
            return False

    def pagina_atual(self):
        if self.atual:
            print(f"📄 Página atual: {self.atual.pagina}")
            return self.atual.pagina
        else:
            print("📄 Nenhuma página visitada.")
            return None

    def exibir_historico_completo(self):
        atual_temp = self.inicio
        historico = []
        while atual_temp:
            marcador = " ← ATUAL" if atual_temp == self.atual else ""
            historico.append(f"{atual_temp.pagina}{marcador}")
            atual_temp = atual_temp.proximo
        print("📋 Histórico completo:", " → ".join(historico))

    def limpar_historico(self):
        self.atual = None
        self.inicio = None
        self.contador = 0
        print("🗑️ Histórico limpo!")

# Simulação prática
print("NAVEGAÇÃO AVANÇADA")
historico = HistoricoNavegacao(limite=5)

historico.visitar("Google")
historico.visitar("YouTube")
historico.visitar("ChatGPT")
historico.visitar("GitHub")
historico.visitar("Stack Overflow")

historico.pagina_atual()
historico.exibir_historico_completo()

print(" Testando navegação")
historico.voltar()
historico.voltar()
historico.avancar()
historico.pagina_atual()

print(" Excedendo limite")
historico.visitar("Nova Página")
historico.exibir_historico_completo()