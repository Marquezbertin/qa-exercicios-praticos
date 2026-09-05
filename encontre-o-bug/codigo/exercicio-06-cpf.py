"""
ENCONTRE O BUG - Exercício 06
Nível: Desafio Final
Tema: Validador de CPF

O algoritmo abaixo valida números de CPF brasileiro.
O código contém BUGS. Sua missão é encontrá-los e corrigi-los.

ALGORITMO OFICIAL DO CPF:
1. Um CPF tem 11 dígitos
2. Todos os dígitos iguais (ex: 111.111.111-11) são INVÁLIDOS
3. Cálculo do 1º dígito verificador:
   - Multiplique os 9 primeiros dígitos por pesos 10, 9, 8, 7, 6, 5, 4, 3, 2
   - Some tudo
   - Resto = (soma * 10) % 11
   - Se resto == 10, o dígito verificador é 0
   - Compare com o 10º dígito do CPF
4. Cálculo do 2º dígito verificador:
   - Multiplique os 10 primeiros dígitos por pesos 11, 10, 9, 8, 7, 6, 5, 4, 3, 2
   - Some tudo
   - Resto = (soma * 10) % 11
   - Se resto == 10, o dígito verificador é 0
   - Compare com o 11º dígito do CPF
5. Somente dígitos são aceitos (considerar formatação 000.000.000-00)
6. Strings vazias ou com menos de 11 dígitos são inválidas

Teste com CPFs conhecidos:
- 529.982.247-25 é VÁLIDO
- 111.111.111-11 é INVÁLIDO
- 123.456.789-09 é VÁLIDO

Dica: há pelo menos 4 bugs escondidos. Execute os testes abaixo para encontrá-los.
"""

import re


def validar_cpf(cpf):
    # Remove não-dígitos
    cpf = re.sub(r"\D", "", cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    # Cálculo 1º dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0

    if resto != int(cpf[9]):
        return False

    # Cálculo 2º dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (10 - i)

    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0

    if resto != int(cpf[10]):
        return False

    return True


# ============ TESTES ============
def testar():
    casos = [
        # (cpf, esperado)
        ("529.982.247-25", True),   # válido conhecido
        ("123.456.789-09", True),   # válido conhecido
        ("111.111.111-11", False),  # todos iguais
        ("000.000.000-00", False),  # todos iguais
        ("52998224725", True),      # sem máscara
        ("123.456.789-10", False),  # dígito verificador errado
        ("111", False),             # curto
        ("", False),                # vazio
        ("529.982.247-2X", False),  # caractere inválido
        ("5299822472", False),      # só 10 dígitos
    ]

    todos_passaram = True
    for cpf, esperado in casos:
        resultado = validar_cpf(cpf)
        status = "PASSOU" if resultado == esperado else "FALHOU"
        if resultado != esperado:
            todos_passaram = False
        print(f"CPF={cpf!r:<20} esperado={str(esperado):<5} obteve={str(resultado):<5} -> {status}")

    if todos_passaram:
        print("\nTodos os testes passaram! Bom trabalho!")
    else:
        print("\nAlguns testes falharam. Encontre e corrija os bugs.")


if __name__ == "__main__":
    testar()