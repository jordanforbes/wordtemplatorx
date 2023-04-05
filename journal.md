##4-3-23

goals: create a python script that outputs a word document from a template. The UI must allow someone to input the replacements, and then the output will be a .docx file with the changes

installed docxtpl python library

docs: https://docxtpl.readthedocs.io/en/latest/
tutorial: https://www.youtube.com/watch?v=_jGVv_rvla8

--for some reason the main.py file sends up an error for docxtpl which is worrying

created a word document template called pytemplate.docx with the variables TEST1 and TEST2

success! It seems to work. I can easily generate documents from a temlplate. All that needs to happen now is to clean it up and make it usable by someone who can't use python. Ideally I'd like it to scan the document and find each individual variable.

used the input() function to generate the variable inputs on the command line

-find way to overwrite, or throw up an error if doc is overwritten
--pseudocode: if there is a name that matches the file name in outputs, then throw error and rerun script

##4/4/23

now is the time to read through a template file and find all of the jinja2 lines
by using the docx module and a regex pattern I was able to find all jinja2 variables in the template

It does indeed now pick up the included variables

currently what can happen is the script scans a word document,
puts the variables into an object,
asks for the name of the file,
outputs a file with empty values

used a for loop that goes through the context object and asks for an input on each line

installed dearpygui to handle, well, the gui
pasted in example code from the github

##4/5/23
created isDuplicate() function in reader.py which makes sure a file name isn't already in the output directory

used coverletter to test the variable checker, checking each paragraph run

used dictionary so now the template can be selected using numbers instead of typing in the entire name of the template file

started creating Reader object in order to consolidate other methods and variables to make it easier for transfer to gui
