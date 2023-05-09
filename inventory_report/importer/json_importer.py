from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if not path.lower().endswith('.json'):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            list = json.load(file)
        return list
