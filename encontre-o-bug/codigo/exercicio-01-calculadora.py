"""
ENCONTRE O BUG - Exercício 01
Nível: Iniciante
Tema: Calculadora de descontos

A função abaixo calcula o valor final de um produto após aplicar um desconto.
O código contém BUGS. Sua missão é encontrá-los e corrigi-los.

REGRAS DO NEGÓCIO:
- Desconto deve ser um valor entre 0 e 100 (porcentagem)
- Preço deve ser maior que zero
- O desconto máximo permitido em promoções é 50%
- Preços negativos devem ser rejeitados
- Se desconto for inválido (> 100 ou < 0), lançar ValueError

Escreva uma função que atenda às regras acima e identifique o que está
errado no código abaixo.

Dica: há pelo menos 3 bugs escondidos.
"""

def calcular_desconto(preco, percentual_desconto):
    if percentual_desconto < 0 or percentual_desconto > 50:
        raise ValueError("Desconto inválido")

    if preco < 0:
        raise ValueError("Preço inválido")

    valor_desconto = preco * (percentual_desconto / 100)
    preco_final = preco - valor_desconto

    return preco_final


# ============ TESTES ============
def testar():
    casos = [
        # (preco, desconto, esperado)
        (100, 10, 90),       # desconto normal
        (50, 50, 25),        # desconto máximo
        (0, 10, None),       # preço zero DEVE ser rejeitado (regra: preço > 0)
        (100, 100, None),    # desconto 100% (deveria falhar!)
        (-10, 10, None),     # preço negativo (deveria falhar!)
        (100, 60, None),     # desconto acima de 50 (deveria falhar!)
    ]

    for preco, desconto, esperado in casos:
        try:
            resultado = calcular_desconto(preco, desconto)
            status = "PASSOU" if resultado == esperado else f"FALHOU (esperado={esperado}, obteve={resultado})"
            print(f"preco={preco}, desconto={desconto} -> {status}")
        except ValueError as e:
            status = "PASSOU" if esperado is None else f"FALHOU (não deveria lançar erro: {e})"
            print(f"preco={preco}, desconto={desconto} -> {status}")
        except Exception as e:
            print(f"preco={preco}, desconto={desconto} -> ERRO INESPERADO: {e}")


if __name__ == "__main__":
    testar()