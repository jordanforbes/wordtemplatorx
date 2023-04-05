import re
import docx
import os

# gets all template files for easier entry

class Reader:
  def __init__(self):
    self.t_dir_path = './templates'
    self.o_dir_path = './outputs'
    self.template_dir = {}
    self.output_dir = []
    self.get_templates()
    print('reader obj test')
    print(self.template_dir)
    self.get_outputs()
    print(self.output_dir)

  def get_templates(self):
    pattern = r'^~\$.*'
    i = 0
    for filename in os.listdir(self.t_dir_path):
        if not re.match(pattern, filename):
          self.template_dir[f'{i}']=filename
          i +=1;
    return self

  def get_outputs(self):
      pattern = r'^~\$.*'
      # add files in directory to obj Array
      for filename in os.listdir(self.o_dir_path):
        if not re.match(pattern, filename):
          self.output_dir.append(filename)
      return self

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

  # def new_file(self, filename):
  #   # isUnique = True;
  #   if filename not in self.output_dir:


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
