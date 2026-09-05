"""
ENCONTRE O BUG - Exercício 02
Nível: Intermediário
Tema: Sistema bancário - Transferência

A classe abaixo representa um sistema de transferência bancária.
O código contém BUGS. Sua missão é encontrá-los e corrigi-los.

REGRAS DO NEGÓCIO:
- Conta deve ter saldo suficiente para transferir (sem cheque especial)
- Valor da transferência deve ser maior que zero
- Não é permitido transferir para a mesma conta
- Existe uma taxa de 2% sobre transferências acima de R$ 1.000,00
- A taxa deve ser cobrada do REMETENTE
- Saldo nunca pode ficar negativo
- A conta de destino deve existir (referência válida)

Dica: há pelo menos 4 bugs escondidos.
"""

class ContaBancaria:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
        return self.saldo


class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero, titular, saldo=0.0):
        if numero in self.contas:
            raise ValueError("Conta já existe")
        self.contas[numero] = ContaBancaria(numero, titular, saldo)
        return self.contas[numero]

    def transferir(self, origem_num, destino_num, valor):
        if valor <= 0:
            raise ValueError("Valor de transferência deve ser maior que zero")

        origem = self.contas.get(origem_num)
        destino = self.contas.get(destino_num)

        if origem is None or destino is None:
            raise ValueError("Conta não encontrada")

        if origem_num == destino_num:
            raise ValueError("Não é possível transferir para a mesma conta")

        # Calcula taxa de 2% para valores acima de 1000
        taxa = 0
        if valor > 1000:
            taxa = valor * 0.02

        # BUG INTENCIONAL: a taxa é DESCONTADA do destinatário
        # (regra: a taxa deve ser cobrada do REMETENTE)
        origem.sacar(valor)
        destino.depositar(valor - taxa)

        return {"taxa": taxa, "saldo_origem": origem.saldo, "saldo_destino": destino.saldo}


# ============ TESTES ============
def testar():
    banco = Banco()
    c1 = banco.criar_conta("001", "João", 5000)
    c2 = banco.criar_conta("002", "Maria", 100)

    print("--- Teste 1: Transferência normal ---")
    try:
        resultado = banco.transferir("001", "002", 500)
        print(f"João saldo: {resultado['saldo_origem']}, Maria saldo: {resultado['saldo_destino']}")
        assert resultado["saldo_origem"] == 4500, "Saldo de João deveria ser 4500"
        assert resultado["saldo_destino"] == 600, "Saldo de Maria deveria ser 600"
        print("PASSOU")
    except Exception as e:
        print(f"FALHOU: {e}")

    print("--- Teste 2: Transferência com taxa (acima de 1000) ---")
    try:
        resultado = banco.transferir("001", "002", 2000)
        # João tem 4500, transferir 2000 + taxa 40 = 2040 -> saldo 2460
        print(f"João saldo: {resultado['saldo_origem']}, Maria saldo: {resultado['saldo_destino']}, taxa: {resultado['taxa']}")
        assert resultado["saldo_origem"] == 2460, "Saldo de João deveria ser 2460"
        assert resultado["saldo_destino"] == 2600, "Saldo de Maria deveria ser 2600"
        assert resultado["taxa"] == 40, "Taxa deveria ser 40"
        print("PASSOU")
    except Exception as e:
        print(f"FALHOU: {e}")

    print("--- Teste 3: Transferência com saldo insuficiente ---")
    try:
        banco.transferir("001", "002", 10000)
        print("FALHOU: Deveria lançar erro de saldo insuficiente")
    except ValueError as e:
        print(f"PASSOU: Erro capturado ({e})")

    print("--- Teste 4: Transferência de valor negativo ---")
    try:
        banco.transferir("001", "002", -100)
        print("FALHOU: Deveria lançar erro de valor inválido")
    except ValueError as e:
        print(f"PASSOU: Erro capturado ({e})")

    print("--- Teste 5: Transferência para conta inexistente ---")
    try:
        banco.transferir("001", "999", 100)
        print("FALHOU: Deveria lançar erro de conta não encontrada")
    except ValueError as e:
        print(f"PASSOU: Erro capturado ({e})")


if __name__ == "__main__":
    testar()