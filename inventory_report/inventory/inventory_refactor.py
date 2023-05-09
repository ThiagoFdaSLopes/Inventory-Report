from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer) -> None:
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        conteudo = self.importer.import_data(path)
        self.data += conteudo
        if type == "simples":
            data = SimpleReport.generate(conteudo)
            return data
        if type == "completo":
            data = CompleteReport.generate(conteudo)
            return data

    def __iter__(self):
        return InventoryIterator(self.data)
