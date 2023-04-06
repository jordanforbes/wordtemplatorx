# gets all template files for easier entry

class Reader:
  def __init__(self):
    self.t_dir_path = './templates'
    self.o_dir_path = './outputs'
    self.templates = {}
    self.outputs = []
    self.set_templates()
    self.set_outputs()
    print('reader debug')
    print(self.templates)
    print(self.outputs)


  def set_templates(self):
    pattern = r'^~\$.*'
    i = 0
    for filename in os.listdir(self.t_dir_path):
        if not re.match(pattern, filename):
          self.templates[f'{i}']=filename
          i +=1;
    return self

  def get_templates(self):
     return self.templates

  def add_template(self, temp):
      return self


  def set_outputs(self):
      pattern = r'^~\$.*'
      # add files in directory to obj Array
      for filename in os.listdir(self.o_dir_path):
        if not re.match(pattern, filename):
          self.outputs.append(filename)
      return self

  def get_outputs(self):
     return self.outputs


  def get_vars(self,file):
      return self

  def set_vars(self,file):
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


  # def isUnique(fileName):
  #   newFile = f'{fileName}.docx'
  #   dir_path = "./outputs"
  #   files = []

  #   # add files in directory to array
  #   for filename in os.listdir(dir_path):
  #     files.append(filename)

  #   if newFile in files:
  #     return False;
  #   else:
  #     return True

  # def new_file(self, filename):
  #   # isUnique = True;
  #   if filename not in self.output_dir:

