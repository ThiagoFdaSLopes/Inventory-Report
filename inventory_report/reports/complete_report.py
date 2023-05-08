from inventory_report.reports.simple_report import SimpleReport
from abc import abstractmethod


class CompleteReport(SimpleReport):
    def generate(list):
        menor_date = SimpleReport.menor_date(list)
        data_validade = SimpleReport.min_date(list)
        empresa_produtos = SimpleReport.count_empresa(list)
        list_empresas = CompleteReport.count_products(list)
        list_names = ""
        for empresa, quantidade in list_empresas.items():
            list_names += f"- {empresa}: {quantidade}\n"

        return f"""Data de fabricação mais antiga: {menor_date}
Data de validade mais próxima: {data_validade}
Empresa com mais produtos: {empresa_produtos}
Produtos estocados por empresa:
{list_names}
"""

    @abstractmethod
    def count_products(list):
        contagem_empresas = {}

        for produto in list:
            empresa = produto["nome_da_empresa"]
            if empresa in contagem_empresas:
                contagem_empresas[empresa] += 1
            else:
                contagem_empresas[empresa] = 1

        return contagem_empresas
