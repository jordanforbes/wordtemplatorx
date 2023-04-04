import re
import docx

def reader():
  # Load the Word document
  doc = docx.Document('templates/pytemplate.docx')

  # Get all the paragraphs in the document
  paragraphs = doc.paragraphs
  context = {}

  pattern = r'{{\s*(.*?)\s*}}'

  # Loop through each paragraph and print the text
  for paragraph in paragraphs:
      text = paragraph.text
      variables = re.findall(pattern, text)
      if variables:
          context.update({f'{variables[0]}':''})
  return context
