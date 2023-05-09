from abc import ABC
from datetime import date, datetime


class SimpleReport(ABC):
    @staticmethod
    def generate(list):

        menor_data = SimpleReport.menor_date(list)
        data_mais_proxima = SimpleReport.min_date(list)
        empresa_mais_produtos = SimpleReport.count_empresa(list)

        return f"""Data de fabricação mais antiga: {menor_data}
Data de validade mais próxima: {data_mais_proxima}
Empresa com mais produtos: {empresa_mais_produtos}"""

    @staticmethod
    def menor_date(lista):
        datas_de_fabricacao = [
            datetime.strptime(
                prod["data_de_fabricacao"],
                "%Y-%m-%d").date() for prod in lista]

        menor_data = min(datas_de_fabricacao)
        return menor_data

    @staticmethod
    def min_date(list):
        data_atual = date.today()
        diferenca_dias_minima = float('inf')
        data_mais_proxima = None
        for produto in list:
            data_validade = datetime.strptime(
                produto["data_de_validade"], "%Y-%m-%d").date()
            diferenca_dias = abs(data_validade - data_atual).days
            if diferenca_dias < diferenca_dias_minima:
                diferenca_dias_minima = diferenca_dias
                data_mais_proxima = data_validade
        return data_mais_proxima

    @staticmethod
    def count_empresa(list):
        contagem_empresas = {}

        for produto in list:
            empresa = produto["nome_da_empresa"]
            if empresa in contagem_empresas:
                contagem_empresas[empresa] += 1
            else:
                contagem_empresas[empresa] = 1

        empresa_mais_produtos = max(
            contagem_empresas, key=contagem_empresas.get)
        return empresa_mais_produtos
