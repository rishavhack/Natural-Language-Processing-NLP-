from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import csv
import re
import numpy as np
import nltk
import spacy
from nltk.corpus import stopwords
import datefinder
#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 

resume_string = convert("resume4.pdf")
resume_string1 = resume_string

def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]
def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

def links(string):
    regex=ur"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
    url = re.findall(regex, string)
    return url 

def extract_name(string):
    r1 = unicode(string,'utf-8')
    nlp = spacy.load('en')
    doc_2 = nlp(r1)
    for ent in doc_2.ents:
        if ent.label_ == "PERSON":
            print('{}'.format(ent))
            break
        
def noOfExperienceFinder():
    noOfexperience = []
    for i in range(len(lines)):
        if 'experience' in lines[i]:
            noOfexperience.append(i)
    if len(noOfexperience)==0:
        return 'Fresher'
    experience = []
    yearsOrMonths = []
    for i in range(len(noOfexperience)):
        if 'year' in lines[noOfexperience[i]]:
            experience.append(lines[noOfexperience[i]])
            yearsOrMonths.append('years')
        elif 'month' in lines[noOfexperience[i]]:
            experience.append(lines[noOfexperience[i]])
            yearsOrMonths.append('months')
        elif 'years' in lines[noOfexperience[i]]:
            experience.append(lines[noOfexperience[i]])
            yearsOrMonths.append('years')
        elif 'months' in lines[noOfexperience[i]]:
            experience.append(lines[noOfexperience[i]])
            yearsOrMonths.append('months')
    
    experienced = []
    if len(experience):
        tagged = nltk.pos_tag(experience[0])
        entities = nltk.chunk.ne_chunk(tagged)
        for subtree in entities.subtrees():
        	for leaf in subtree.leaves():
        		if leaf[1] == 'CD':
        			experienced.append(leaf[0] +' '+yearsOrMonths[0])
        return experienced[0]

def technicalSkills():
    skills = []
    for word in resume_string1.split(" "):
        if word in set(your_list[0]):
            skills.append(word.encode('ascii', 'ignore'))
    skills1 = list(set(skills))
    return skills1

def nonTechnical():
    nontechskills = []
    for word in resume_string1.split(" "):
        if word in set(your_list1[0]):
            nontechskills.append(word.encode('ascii', 'ignore'))
    nontechskills = set(nontechskills)
    list5 = list(nontechskills)
    return list5  

def dob():
    dob = [];
    matches = datefinder.find_dates(resume_string1)
    for match in matches:
        print match
    
print "Mobile No -", extract_phone_numbers(resume_string1)
print "Email Id -",extract_email_addresses(resume_string1)
print "Links -",links(resume_string1)
print "Name -",extract_name(resume_string1)

resume_string1 =resume_string1.lower()
resume_string1 =unicode(resume_string1,'utf-8')
lines = [el.strip() for el in resume_string1.split("\n") if len(el)>0]
lines = [nltk.word_tokenize(el) for el in lines]

print "Experience -",noOfExperienceFinder()
resume_string3 = resume_string1.replace(',',' ')

with open('techskill.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)
with open('nontechnicalskills.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list1 = list(reader)

print "Skills -",technicalSkills()
print "Non Tec - ",nonTechnical()
print "Date Of birth",dob()
