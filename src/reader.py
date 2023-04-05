import re
import docx
import os

# gets all template files for easier entry
def getTemplates():
    dir_path = './templates'
    tempDir = {}
    pattern = r'^~\$.*'
    i = 0
    for filename in os.listdir(dir_path):
        if not re.match(pattern, filename):
          tempDir[f'{i}']=filename
          i +=1;
    # print(tempDir)
    return tempDir



# checks if the name you gave your file already exists
def isUnique(fileName):
  newFile = f'{fileName}.docx'
  dir_path = "./outputs"
  files = []

  # add files in directory to array
  for filename in os.listdir(dir_path):
    files.append(filename)

  if newFile in files:
    return False;
  else:
    return True



def getVariables(file):
  # Load the Word document
  doc = docx.Document(f'templates/{file}')

  paragraphs = doc.paragraphs
  context = {}

  pattern = r'{{\s*(.*?)\s*}}'

  for paragraph in paragraphs:
      for run in paragraph.runs:
          text = run.text
          variables = re.findall(pattern, text)
          if variables:
              context.update({f'{variables[0]}':''})
  return context
