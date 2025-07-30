import spacy #spacy

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