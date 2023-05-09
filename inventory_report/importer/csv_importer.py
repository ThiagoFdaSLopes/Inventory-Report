from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if not path.lower().endswith('.csv'):
            raise ValueError("Arquivo inválido")
        with open(path, newline="") as file:
            dados = csv.DictReader(file)
            list_dados = list(dados)
        return list_dados
