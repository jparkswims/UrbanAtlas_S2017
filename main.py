import codecs
import spacy
nlp = spacy.load('en')

def main():

    LOCS = []
    locs = []
    flag = False
    
    fileNames = ['NewYorkGaslight.txt','NewYorkSlices.txt','Bartleby.txt','whitman-leaves.txt']

    for filename in fileNames:
        file = codecs.open(filename,'r','utf-8')
        textraw = file.read()
        text = nlp(textraw)

        gpes = obtainGPEs(text)

        for gpe in gpes:

            if not gpe.upper() in locs:
                locs.append(gpe.upper())
                LOC = Location(gpe.upper())
                LOCS.append(LOC)

            lind = locs.index(gpe.upper())
                
            adjs = adjectivesDescribingPlaces(text,gpe)

            for adj in adjs:

                if not adj.lower() in LOCS[lind].adjectives:
                    LOCS[lind].adjectives.append(adj.lower())
                    ADJ = Adjective(adj.lower())
                    LOCS[lind].ADJS.append(ADJ)
                    flag = False
                else:
                    flag = True

                aind = LOCS[lind].adjectives.index(adj.lower())

                if flag:
                    LOCS[lind].ADJS[aind].incCount()

    #file write here
    file1 = open('ALLTEXT_ADJS.txt','w',encoding='utf-8')

    for LOC in LOCS:
        LOC.clean()
        LOC.sortADJS()
        file1.write(LOC.toString())

    file1.close()
              
class Location:

    def __init__(self,name):
        self.name = name
        self.adjectives = []
        self.ADJS = []

    def addAdj(self,adj,ADJ):
        self.adjectives.append(adj)
        self.ADJS.append(ADJ)

    def toString(self):
        limit = 10
        count = 0
        outstr = self.name + "\n"
        for adj in self.ADJS:
            outstr += adj.toString()
            count += 1
            if count == limit:
                break
        outstr += "\n"
        return outstr

    def clean(self):
        for ADJ in self.ADJS:
            exclude = ["which","much","which","whose","its","his","hers","your","their","our","all","such","that"]
            if ADJ.name.lower() in exclude:
                self.ADJS.remove(ADJ)
            

    def sortADJS(self):
        while True:
            swaps = 0;
            for ind in range(len(self.ADJS)-1):
                if (self.ADJS[ind].count < self.ADJS[ind+1].count):
                    temp = self.ADJS[ind]
                    self.ADJS[ind] = self.ADJS[ind+1]
                    self.ADJS[ind+1] = temp
                    swaps += 1
            if swaps == 0:
                break
            
        
def adjectivesDescribingPlaces(text, gpe):
    sents = [sent for sent in text.sents if gpe in sent.string]
    adjectives = []
    for sent in sents: 
        for word in sent:
            if word.pos_ == 'ADJ':
                adjectives.append(word.string.strip())
            #if gpe in word.string:
                #for child in word.children: 
                    #if child.pos_ == 'ADJ': 
                        #adjectives.append(child.string.strip())
    return adjectives

class Adjective:

    def __init__(self,name):
        self.name = name
        self.count = 1

    def incCount(self):
        self.count += 1

    def toString(self):
        outstr = self.name + " " + str(self.count) + "\n"
        return outstr

def obtainGPEs(text):
    allGPEs = [ent for ent in text.ents if ent.label_ == 'GPE']
    gpes = []
    for word in allGPEs:
        if not (word.string.strip() in gpes):
            gpes.append(word.string.strip())
    if '' in gpes:
        gpes.remove('')
    if 'the' in gpes:
        gpes.remove('the')
    return gpes

######################################
main()
