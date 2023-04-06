from docxtpl import DocxTemplate
from pathlib import Path
from filecmp import cmp
import re
import docx
import os
# from itertools import tee, islice, chain

# def previous_and_next(some_iterable):
#     prevs, items, nexts = tee(some_iterable, 3)
#     prevs = chain([None], prevs)
#     nexts = chain(islice(nexts, 1, None), [None])
#     return zip(prevs, items, nexts)

# mylist = 'bannana and {{ raybans }}'

# for previous, item, nxt in previous_and_next(mylist):
#     print(f"Item is now {item}, next is {nxt}, previous is {previous}")

# class for an individual template document, contains context variables
class TemplClass:
    def __init__(self, fileName):
        self.path = f'../templates/{fileName}'
        self.doc = docx.Document(self.path)
        self.context = {} #variables
        self.init_context()
        print(self.path)
        print(self.context)

    # reads template document to get variables
    def init_context(self):
        paragraphs = self.doc.paragraphs
        pattern = r'{{\s*(.*?)\s*}}'

        def findVars(pattern, text):
            variable = re.findall(pattern, text)
            if variable:
                self.context.update({f'{variable[0]}':''})
                print(text)
        for paragraph in paragraphs:
            text = paragraph.text
            findVars(pattern, text)
        print(self.context)
        return self

# CLT= TemplClass('coverlettertemplate.docx')


# should be able to find multiple variables within the same runs
testStr = 'I am {{ testing }} this {{ run }}'
prevLetter = ''
currentLetter = ''
inVar = False
testVar = ''
testArr = []

for l in testStr:
    prevLetter = currentLetter
    currentLetter = l
    print(prevLetter,currentLetter, inVar, testVar)
    if currentLetter and prevLetter == '{':
        inVar = True
        # testVar += '{'
    elif currentLetter and prevLetter == '}':
        # testVar += '}'
        if not testVar == '':
            testArr.append('{'+testVar+'}')
            print('sent here!')
            testVar = ''
            inVar = False
    if inVar:
        testVar += currentLetter

print(testArr)
