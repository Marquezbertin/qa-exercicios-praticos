"""
ENCONTRE O BUG - Exercício 05
Nível: Avançado
Tema: Processamento de dados com datas

A função abaixo processa eventos com datas e status.
O código contém BUGS. Sua missão é encontrá-los e corrigi-los.

REGRAS DO NEGÓCIO:
1. Data deve estar no formato YYYY-MM-DD
2. A data do evento não pode ser no futuro
3. Status válidos: "PENDENTE", "EM_PROCESSO", "CONCLUIDO", "CANCELADO"
4. Um evento CONCLUIDO não pode ser alterado para CANCELADO
5. Um evento CANCELADO não pode receber nova data
6. Eventos PENDENTES com mais de 30 dias devem estar com status "VENCIDO"
   (o "VENCIDO" é derivado, não armazenado)
7. Ao comparar datas, um mês tem entre 28 e 31 dias (use datetime corretamente)
8. A lista de eventos não pode conter duplicatas (mesmo id)

Dica: há pelo menos 5 bugs escondidos.
"""

from datetime import datetime, timedelta


class GerenciadorEventos:
    def __init__(self):
        self.eventos = {}

    def adicionar_evento(self, id_evento, data, status="PENDENTE"):
        if id_evento in self.eventos:
            raise ValueError("Evento duplicado")

        if status not in ["PENDENTE", "EM_PROCESSO", "CONCLUIDO", "CANCELADO"]:
            raise ValueError("Status inválido")

        try:
            data_evento = datetime.strptime(data, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Data inválida. Use o formato YYYY-MM-DD")

        if data_evento > datetime.now():
            raise ValueError("Data do evento não pode ser no futuro")

        self.eventos[id_evento] = {
            "data": data,
            "status": status
        }

    def alterar_status(self, id_evento, novo_status):
        if id_evento not in self.eventos:
            raise ValueError("Evento não encontrado")

        if novo_status not in ["PENDENTE", "EM_PROCESSO", "CONCLUIDO", "CANCELADO"]:
            raise ValueError("Status inválido")

        evento = self.eventos[id_evento]

        if evento["status"] == "CONCLUIDO" and novo_status == "CANCELADO":
            raise ValueError("Evento concluído não pode ser cancelado")

        if evento["status"] == "CANCELADO" and novo_status != "CANCELADO":
            raise ValueError("Evento cancelado não pode ser reativado")

        evento["status"] = novo_status

    def alterar_data(self, id_evento, nova_data):
        if id_evento not in self.eventos:
            raise ValueError("Evento não encontrado")

        evento = self.eventos[id_evento]

        if evento["status"] == "CANCELADO":
            raise ValueError("Evento cancelado não pode ter data alterada")

        try:
            data_validada = datetime.strptime(nova_data, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Data inválida. Use o formato YYYY-MM-DD")

        if data_validada > datetime.now():
            raise ValueError("Data do evento não pode ser no futuro")

        evento["data"] = nova_data

    def status_efetivo(self, id_evento):
        """Retorna o status real, calculando VENCIDO quando aplicável."""
        if id_evento not in self.eventos:
            raise ValueError("Evento não encontrado")

        evento = self.eventos[id_evento]
        if evento["status"] == "PENDENTE":
            data_evento = datetime.strptime(evento["data"], "%Y-%m-%d")
            hoje = datetime.now()
            dias = (hoje - data_evento).days
            if dias >= 30:
                return "VENCIDO"
        return evento["status"]

    def listar(self):
        return {id: {"data": e["data"], "status": self.status_efetivo(id)}
                for id, e in self.eventos.items()}


# ============ TESTES ============
def testar():
    print("--- Teste 1: Adicionar evento normal ---")
    g = GerenciadorEventos()
    g.adicionar_evento(1, "2026-08-01")
    assert g.status_efetivo(1) == "VENCIDO", "Evento de agosto já deveria estar VENCIDO (mais de 30 dias)"
    print("PASSOU")

    print("--- Teste 2: Evento recente ---")
    g = GerenciadorEventos()
    g.adicionar_evento(2, "2026-09-01")
    assert g.status_efetivo(2) == "PENDENTE", "Evento recente deveria estar PENDENTE"
    print("PASSOU")

    print("--- Teste 3: Evento duplicado ---")
    g = GerenciadorEventos()
    g.adicionar_evento(1, "2026-09-01")
    try:
        g.adicionar_evento(1, "2026-09-02")
        print("FALHOU: Deveria rejeitar evento duplicado")
    except ValueError:
        print("PASSOU")

    print("--- Teste 4: Data no futuro ---")
    g = GerenciadorEventos()
    try:
        g.adicionar_evento(3, "2030-01-01")
        print("FALHOU: Deveria rejeitar data no futuro")
    except ValueError:
        print("PASSOU")

    print("--- Teste 5: Data inválida ---")
    g = GerenciadorEventos()
    try:
        g.adicionar_evento(4, "31/12/2026")
        print("FALHOU: Deveria rejeitar formato inválido")
    except ValueError:
        print("PASSOU")

    print("--- Teste 6: Concluído não pode cancelar ---")
    g = GerenciadorEventos()
    g.adicionar_evento(5, "2026-09-01", "CONCLUIDO")
    try:
        g.alterar_status(5, "CANCELADO")
        print("FALHOU: Concluído não pode ser cancelado")
    except ValueError:
        print("PASSOU")

    print("--- Teste 7: Cancelado não pode reativar ---")
    g = GerenciadorEventos()
    g.adicionar_evento(6, "2026-09-01", "CANCELADO")
    try:
        g.alterar_status(6, "PENDENTE")
        print("FALHOU: Cancelado não pode ser reativado")
    except ValueError:
        print("PASSOU")

    print("--- Teste 8: Cancelado não pode mudar data ---")
    g = GerenciadorEventos()
    g.adicionar_evento(7, "2026-09-01", "CANCELADO")
    try:
        g.alterar_data(7, "2026-09-05")
        print("FALHOU: Cancelado não pode mudar data")
    except ValueError:
        print("PASSOU")

    print("--- Teste 9: Limite de 30 dias (dia 31) ---")
    g = GerenciadorEventos()
    data_31_dias = (datetime.now() - timedelta(days=31)).strftime("%Y-%m-%d")
    g.adicionar_evento(8, data_31_dias)
    assert g.status_efetivo(8) == "VENCIDO", f"Deveria estar VENCIDO ({data_31_dias})"
    print("PASSOU")

    print("--- Teste 10: Limite de 30 dias (dia 30) ---")
    g = GerenciadorEventos()
    data_30_dias = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    g.adicionar_evento(9, data_30_dias)
    assert g.status_efetivo(9) == "PENDENTE", f"Deveria estar PENDENTE ({data_30_dias})"
    print("PASSOU")


if __name__ == "__main__":
    testar()