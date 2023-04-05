import re
import docx
import os


def isDuplicate(fileName):
  newFile = f'{fileName}.docx'
  dir_path = "./outputs"
  files = []
  # print(newFile)
  # print(files)
  # add files in directory to array
  for filename in os.listdir(dir_path):
    files.append(filename)
  # print(files)
  # check if file exists in directory
  if newFile in files:
    return True;
  else:
    return False

def getVariables(file):
  # Load the Word document
  doc = docx.Document(f'templates/{file}.docx')

  paragraphs = doc.paragraphs
  context = {}

  pattern = r'{{\s*(.*?)\s*}}'
  # def varCheck():
  #   text = paragraph.text
  #   variables = re.findall(pattern, text)
  #   if variables:
  #       varCheck()
  #       context.update({f'{variables[0]}':''})

  for paragraph in paragraphs:
      # print('runtest')
      for run in paragraph.runs:
          # print(run.text)
          # print('---')
      # print(paragraph.text)
          text = run.text
          variables = re.findall(pattern, text)
          if variables:
              context.update({f'{variables[0]}':''})
  return context
