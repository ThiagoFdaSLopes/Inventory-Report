from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto_um = Product(
        1,
        "Cesta",
        "Casa",
        "10-10-2023",
        "10-12-2023", 122344, "na Mesa")

    assert (
        produto_um.__repr__() ==
        "O produto Cesta fabricado em 10-10-2023 por Casa" +
        " com validade até 10-12-2023 precisa ser armazenado na Mesa.")
