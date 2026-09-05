"""
ENCONTRE O BUG - Exercício 03
Nível: Avançado
Tema: Carrinho de compras com frete e cupom

O código abaixo gerencia um carrinho de compras.
O código contém BUGS. Sua missão é encontrá-los e corrigi-los.

REGRAS DO NEGÓCIO:
1. Frete é grátis para pedidos acima de R$ 100,00
2. Frete padrão é R$ 15,00
3. Cupom "QA10" dá 10% de desconto no subtotal
4. Cupom "FRETEGRATIS" remove o frete (mas não pode ser combinado com QA10)
5. Desconto do cupom NUNCA pode deixar o total negativo
6. Quantidade de um item deve ser inteira e maior que zero
7. Itens com preço menor ou igual a zero devem ser rejeitados
8. Se o carrinho está vazio, o total deve ser 0 sem frete

Dica: há pelo menos 5 bugs escondidos (fique atento aos casos limite).
"""

class Item:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


class Carrinho:
    def __init__(self):
        self.itens = []
        self.cupom = None

    def adicionar_item(self, nome, preco, quantidade):
        if preco <= 0:
            raise ValueError("Preço do item deve ser maior que zero")
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        if not isinstance(quantidade, int):
            raise ValueError("Quantidade deve ser um número inteiro")

        self.itens.append(Item(nome, preco, quantidade))

    def aplicar_cupom(self, cupom):
        if cupom not in ["QA10", "FRETEGRATIS"]:
            raise ValueError("Cupom inválido")
        self.cupom = cupom

    def subtotal(self):
        return sum(item.preco * item.quantidade for item in self.itens)

    def frete(self):
        if not self.itens:
            return 0
        if self.subtotal() > 100:
            return 0
        return 15

    def desconto(self):
        if self.cupom == "QA10":
            return self.subtotal() * 0.10
        return 0

    def total(self):
        sub = self.subtotal()
        desc = self.desconto()
        if self.cupom == "FRETEGRATIS":
            fret = 0
        else:
            fret = self.frete()

        total = sub - desc + fret
        if total < 0:
            total = 0
        return total


# ============ TESTES ============
def testar():
    print("--- Teste 1: Carrinho vazio ---")
    c = Carrinho()
    assert c.total() == 0, f"Total deveria ser 0, obteve {c.total()}"
    print("PASSOU")

    print("--- Teste 2: Compra simples abaixo de 100 (frete 15) ---")
    c = Carrinho()
    c.adicionar_item("Mouse", 50, 1)
    assert c.total() == 65, f"Total deveria ser 65, obteve {c.total()}"
    print("PASSOU")

    print("--- Teste 3: Compra acima de 100 (frete grátis) ---")
    c = Carrinho()
    c.adicionar_item("Teclado", 120, 1)
    assert c.total() == 120, f"Total deveria ser 120, obteve {c.total()}"
    print("PASSOU")

    print("--- Teste 4: Cupom QA10 ---")
    c = Carrinho()
    c.adicionar_item("Mouse", 50, 2)  # subtotal 100
    c.aplicar_cupom("QA10")
    # desconto 10 -> 90, + frete grátis (>=100) = 90
    assert c.total() == 90, f"Total deveria ser 90, obteve {c.total()}"
    print("PASSOU")

    print("--- Teste 5: Cupom FRETEGRATIS ---")
    c = Carrinho()
    c.adicionar_item("Cabo HDMI", 30, 1)  # subtotal 30
    c.aplicar_cupom("FRETEGRATIS")
    assert c.total() == 30, f"Total deveria ser 30, obteve {c.total()}"
    print("PASSOU")

    print("--- Teste 6: Quantidade fracionada ---")
    c = Carrinho()
    try:
        c.adicionar_item("Caneta", 10, 2.5)
        print("FALHOU: Deveria rejeitar quantidade fracionada")
    except ValueError:
        print("PASSOU")

    print("--- Teste 7: Quantidade zero ---")
    c = Carrinho()
    try:
        c.adicionar_item("Caneta", 10, 0)
        print("FALHOU: Deveria rejeitar quantidade zero")
    except ValueError:
        print("PASSOU")

    print("--- Teste 8: Preço zero ---")
    c = Carrinho()
    try:
        c.adicionar_item("Brinde", 0, 1)
        print("FALHOU: Deveria rejeitar preço zero")
    except ValueError:
        print("PASSOU")

    print("--- Teste 9: Cupom inválido ---")
    c = Carrinho()
    try:
        c.aplicar_cupom("DESC20")
        print("FALHOU: Deveria rejeitar cupom inválido")
    except ValueError:
        print("PASSOU")

    print("--- Teste 10: Total exatamente 100 (limite frete) ---")
    c = Carrinho()
    c.adicionar_item("Fone", 100, 1)
    assert c.total() == 100, f"Total deveria ser 100, obteve {c.total()}"
    print("PASSOU")

    print("--- Teste 11: Desconto maior que subtotal (não pode ficar negativo) ---")
    c = Carrinho()
    c.adicionar_item("Pilha", 5, 1)  # subtotal 5
    c.aplicar_cupom("QA10")  # desconto 0.50
    # total = 5 - 0.50 + 15 = 19.50 (frete incluído pois < 100)
    assert c.total() == 19.50, f"Total deveria ser 19.50, obteve {c.total()}"
    print("PASSOU")


if __name__ == "__main__":
    testar()