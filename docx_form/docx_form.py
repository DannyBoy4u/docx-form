from io import StringIO
from zipfile import ZipFile
import zipfile
from lxml import etree 


root = etree.Element('html', version="5.0")

# Pass the parent node, name of the child node,
# and any number of optional attributes
etree.SubElement(root, 'head')
etree.SubElement(root, 'title', bgcolor="red", fontsize='22')
etree.SubElement(root, 'body', fontsize="15")
#print (et.tostring(root, pretty_print=True).decode("utf-8"))
print(root.tag)
for e in root:
        print(e.tag)


tree = etree.parse('C:\\Users\\2006S\\411-PythonProject\\docx-form\\docx_form\\document.xml')
tree2: str = "C:\\Users\\2006S\\411-PythonProject\\docx-form\\docx_form\\document.xml"
print(etree.tostring(tree))

for event, element in etree.iterwalk(tree, events=('start', 'end')):
    print(event, element)
    print(event)
    print(element.text)

with open(tree2) as fobj:
    xml = fobj.read()

root = etree.fromstring(xml)

for appt in root.getchildren():
    print(appt.tag + " => " + appt.text)
    for elem in appt.getchildren():
        print(elem.tag + " => " + elem.text)
        for item in elem.getchildren():
            print(item.tag + " => " + item.text)

#document = et.fromstring(et.tostring(tree.getroot()))
#print(document.xpath('/document'))

class DocxForm:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def print_path(self) -> None:
        print(self.file_path)
    
    def parseXML(xmlFile):
        with open(xmlFile) as fobj:
            xml = fobj.read()

        root = etree.fromstring(xml)

        for appt in root.getchildren():
            for elem in appt.getchildren():
                if not elem.text:
                    text = "None"
                else: 
                    text = elem.text
                print(elem.tag + " => " + text)    

# Use this for debugging, then move to a test file.
# This will run if you run this file directly.
if __name__ == "__main__":
    ...
