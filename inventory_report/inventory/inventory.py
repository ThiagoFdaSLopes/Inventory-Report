from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        types_arq = {
            "csv": CsvImporter, "json": JsonImporter, "xml": XmlImporter
        }
        if type == "simples":
            extensao = path.split(".")[1]
            data = SimpleReport.generate(types_arq[extensao].import_data(path))
            return data
        if type == "completo":
            extensao = path.split(".")[1]
            data = CompleteReport.generate(
                types_arq[extensao].import_data(path))
            return data
