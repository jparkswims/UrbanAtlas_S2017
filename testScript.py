import codecs
import spacy
from collections import Counter
nlp = spacy.load('en')

def adjectivesDescribingPlaces(text, gpe):
    sents = [sent for sent in text.sents if gpe in sent.string]
    adjectives = []
    for sent in sents: 
        for word in sent: 
            if gpe in word.string:
                for child in word.children: 
                    if child.pos_ == 'ADJ': 
                        adjectives.append(child.string.strip())
    return adjectives

file = codecs.open('NewYorkSlices.txt','r','utf-8')
textraw = file.read()

text = nlp(textraw)

#textSents = text.sents
gpes = [ent for ent in text.ents if ent.label_ == 'GPE']

adj = adjectivesDescribingPlaces(text,'Broadway')

#tagDict = {w.pos: w.pos_ for w in text} 

#allPropNouns = [w for w in text if w.pos_ == 'PROPN']

#propNouns = [];

#for word in allPropNouns:
    #if not (word.string.strip() in propNouns):
 #       propNouns.append(word.string.strip())

#propNouns.sort()

#allPropNouns = []

#file1 = open('LeavesOfGrass_PROPN.txt','w')

#for word in propNouns:
#    file1.write(word+"\n")

#file1.close()

#propNouns = []

#allEnts = text.ents

#namedEnts = []

#for word in allEnts:
#    if not (word.string.strip() in namedEnts):
#        namedEnts.append(word.string.strip())

#for word in namedEnts:
#    if word.isnumeric():
#        namedEnts.remove(word)
#    if "\n" in word:
#        namedEnts.remove(word)
#    if word == "" or word == '"' or word == "(" or word == ")":
#        namedEnts.remove(word)

#for x in range(len(namedEnts)):
#    if "\n" in namedEnts[x]:
#        namedEnts[x] = namedEnts[x].replace("\n"," ")

#namedEnts.sort()

#allEnts = []       

#file2 = open('LeavesOfGrass_NENT.txt','w')

#for word in namedEnts:
#    file2.write(word+"\n")

#file2.close()
    

#Counter([w.string.strip() for w in propNouns]).most_common(10)

#for words in text:

    #if words.pos_ == 'PROPN':

 #       properNouns.append(words)
        

#set([w.label_ for w in text.ents])

#gpes = [ent for ent in text.ents if ent.label_ == 'GPE']

#for (gpes[0] in text.ents)

    #print(
