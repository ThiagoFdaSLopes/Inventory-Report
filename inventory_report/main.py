import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    try:
        _, path, type = sys.argv
        types_arq = {
            "csv": CsvImporter, "json": JsonImporter, "xml": XmlImporter
        }
        extensao = path.split(".")[1]

        data = InventoryRefactor(types_arq[extensao]).import_data(path, type)
        print(data, end="")
    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
