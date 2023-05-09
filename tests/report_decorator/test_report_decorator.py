from inventory_report.reports.colored_report import ColoredReport
from datetime import datetime, timedelta

import pytest
from faker import Faker

from inventory_report.reports.simple_report import SimpleReport
from tests.factories.product_factory import ProductFactory

faker = Faker("pt-BR")

old_date = faker.past_date()
future_date = faker.future_date() + timedelta(days=20)

oldest_date = old_date - timedelta(days=30)
closest_date = datetime.today().date() + timedelta(days=10)
company_bigger_stock = faker.company()


@pytest.fixture
def stock():
    return [
        vars(
            ProductFactory(
                nome_da_empresa=company_bigger_stock[
                    : len(company_bigger_stock) // 2
                ],
                data_de_fabricacao=str(old_date),
                data_de_validade=str(future_date),
            )
        ),
        vars(
            ProductFactory(
                nome_da_empresa=company_bigger_stock,
                data_de_fabricacao=str(old_date),
                data_de_validade=str(future_date),
            )
        ),
        vars(
            ProductFactory(
                nome_da_empresa=company_bigger_stock,
                data_de_fabricacao=str(old_date),
                data_de_validade=str(old_date),
            )
        ),
        vars(
            ProductFactory(
                nome_da_empresa=company_bigger_stock + " LIMITED",
                data_de_fabricacao=str(oldest_date),
                data_de_validade=str(closest_date),
            )
        ),
    ]

# Feito com ajuda de felipe pinto


def test_decorar_relatorio(stock):
    report = ColoredReport(SimpleReport())
    data = report.generate(stock)
    green_phrases = [
        "Data de fabricação mais antiga:",
        "Data de validade mais próxima:",
        "Empresa com mais produtos:",
    ]
    for phrase in green_phrases:
        assert f"\033[32m{phrase}\033[0m" in data

    assert f"\033[36m{str(closest_date)}\033[0m" in data
    assert f"\033[36m{str(oldest_date)}\033[0m" in data
    assert f"\033[31m{company_bigger_stock}\033[0m" in data
