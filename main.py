import spacy

nlp = spacy.load("en_core_web_sm")

with open("today.txt") as f:
    text = f.read()

#print(text)

# calling en_core_web_sm nlp model
#taking in text as obj
doc = nlp(text)
print(doc)

#text is everything
print(len(text))

#doc obj is valuable and shorter, counts individual tokens, split text into tokens
print(len(doc))

for token in text[0:10]:
    print(token)

for token in doc[:10]:
    print(token)