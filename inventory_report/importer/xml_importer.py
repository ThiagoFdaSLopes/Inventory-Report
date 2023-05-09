from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        if not path.lower().endswith('.xml'):
            raise ValueError("Arquivo inválido")

        tree = ET.parse(path)
        root = tree.getroot()

        data = []
        for element in root:
            item = {}
            for subelement in element:
                item[subelement.tag] = subelement.text
            data.append(item)
        return data
