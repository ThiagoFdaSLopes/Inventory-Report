from inventory_report.inventory.product import Product
from datetime import date


def test_cria_produto():
    id = 1
    nome_da_empresa = "Americanas"
    nome_do_produto = "Caixa de Ovos"
    data_de_fabricacao = date(2023, 2, 10)
    data_de_validade = date(2023, 6, 10)
    numero_de_serie = "123456"
    instrucoes_de_armazenamento = "Guarda em local Fresco"
    produto_um = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade, numero_de_serie, instrucoes_de_armazenamento)

    assert produto_um.id == 1
    assert produto_um.nome_do_produto == nome_do_produto
    assert produto_um.nome_da_empresa == nome_da_empresa
    assert (produto_um.data_de_fabricacao
            == data_de_fabricacao.strftime("%Y-%m-%d"))
    assert produto_um.data_de_validade == data_de_validade.strftime("%Y-%m-%d")
    assert produto_um.numero_de_serie == numero_de_serie
    assert (produto_um.instrucoes_de_armazenamento
            == instrucoes_de_armazenamento)
