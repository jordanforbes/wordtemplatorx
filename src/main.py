from docxtpl import DocxTemplate
from pathlib import Path
from filecmp import cmp
from reader import isUnique, getVariables, getTemplates
from gui import gui

def main():
  # gui()
  allTemplates = getTemplates()
  print(allTemplates)
  print('which template are you using?')
  templateKey = input()

  templateName = ''
  if allTemplates[templateKey]:
    templateName = allTemplates[templateKey]
  else:
    print('template not found')
    main()

  print(f'selected template: {templateName}')
  context = getVariables(templateName)
  print('name of file:')
  name = input("")
  if isUnique(name):
    for k in context.keys():
      print(f'input text for {k}')
      context[k] = input()
    doc = DocxTemplate(f"templates/{templateName}")
    doc.render(context)
    doc.save(f"outputs/{name}.docx")
    print(f'file saved successfully')
  else:
    print('that file already exists')
    main()



main()
