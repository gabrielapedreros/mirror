#learning document for spacy
import spacy #spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm") # calling en_core_web_sm nlp model

with open("today.txt") as f:
    text = f.read()
#print(text) #make sure its reading the correct file

doc = nlp(text) #taking in text as obj
print(doc) #all the text from the file will print

print(len(text)) #length of the entire document text

#doc obj is valuable and shorter, counts individual tokens, split text into tokens
print(len(doc)) #length is shorter

for token in text[0:10]:
    print(token) #prints each letter

for token in doc[0:10]:
    print(token) #prints each word or token
#^ each individual token has attributes and metadata in it

#spacy now can separate each sentence using
#the period but its beyond period, from doc obj that would
#take hours of code
for sent in doc.sents:
    print(sent)

#must create list in order to iterate bc 
#sentence is a generator 
sentence1 = list(doc.sents)[0] #first sentence
print (sentence1)

token2 = sentence1[2]
print(token2)
#looks like a string, but its been passed throught the model

#ent_type_: type ,example: geopolitical entity
#lemma: verb
#morph: morphalogical analysis, past verb
#pos_: part of speech 

print(token2.morph)
print(token2.pos_)
print(token2.dep_)
print(token2.lang_)

for token in sentence1:
    print (token.text,token.pos_, token.dep_) #sentence semantics

displacy.render(sentence1, style="dep")