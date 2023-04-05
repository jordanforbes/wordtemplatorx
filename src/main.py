from docxtpl import DocxTemplate
from pathlib import Path
from filecmp import cmp
from reader import isDuplicate, getVariables
from gui import gui

def main():
  # gui()
  print('which template are you using?')
  templateName = input()
  context = getVariables(templateName)
  # print(context)
  print('name of file:')
  name = input("")
  if isDuplicate(name) == False:
    for k in context.keys():
      print(f'input text for {k}')
      context[k] = input()
    doc = DocxTemplate(f"templates/{templateName}.docx")
    doc.render(context)
    doc.save(f"outputs/{name}.docx")
  else:
    print('that file already exists')
    main()



main()
