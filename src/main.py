from docxtpl import DocxTemplate
from pathlib import Path
from filecmp import cmp
from reader import reader

# def contextBuilder():
#   context = {}
# text = None
# name = None
# input text on command line
def main():
  context = reader()
  print(context)
  print('name of file:')
  name = input("")
  # print("text to enter into text1")
  # text1 = input("")
  # print("text to enter into text2")
  # text2 = input("")
  doc = DocxTemplate("templates/pytemplate.docx")
  doc.render(context)
  doc.save(f"outputs/{name}.docx")



main()
