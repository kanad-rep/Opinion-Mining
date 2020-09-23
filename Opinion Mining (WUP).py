#Importing the libraries

import pandas as pd
import nltk
import string
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from collections import Counter

#Reading the file

file = pd.read_excel("E:/Work/Machine Learning/Assignments/Assignment 2/pm_qualities_data.xlsx", sheet_name = "Sheet1")
file.columns = ["Data"]

#Extracting the words

l1 = []
for index, row in file.iterrows():
    words = row["Data"].split(" ")
    for j in words:
        l1.append(j.lower())

#Removing punctuations and stopwords
        
def punc(text):
    exclude = set(string.punctuation)
    text = [''.join(x for x in y if x not in exclude) for y in text]
    text = [x for x in text if x not in stopwords.words('english')]
    return text

l1 = punc(l1)

#Creating the temporary vocabulary of nouns and adjectives

POS = ['JJ','JJR','JJS','NN','NNS','NNP','NNPS']
temp_vocab = sorted([word for (word,pos) in nltk.pos_tag(l1) if pos in POS])
df1 = pd.DataFrame(columns = ["Words", "Frequency"])
c1 = Counter(temp_vocab)
df1["Words"] = c1.keys()
df1["Frequency"] = c1.values()
df1 = df1.sort_values(by = ["Frequency"], ascending = False)
df1.to_csv(r"E:/Work/Machine Learning/Assignments/Assignment 2/Result1.csv", sep = ',')

#Finding the synsets and derivationally related forms containing nouns and adjectives

def syn(text):
    s = []
    for w in text:
        i = wn.synsets(str(w),pos = 'n')
        j = wn.synsets(str(w), pos = 'a')
        if i!=[]:
            s.append(i)
        if j !=[]:
            s.append(j)
    return s

s1 =syn(temp_vocab)

d1 = []
for sy in s1:
    for a in sy:
        for k in a.lemmas():
            for z in k.derivationally_related_forms():
                    d1.append(z.name())

s2 = syn(d1)

#Creating the main vocabulary

vocab = []
for i in s1:
    for j in i:
        vocab.append(j)
for i in s2:
    for j in i:
        vocab.append(j)
vocab = sorted(set(vocab))

#Calculating the similarities between the synsets

def sim(mat):
    thres = 0.8
    l = []
    for i in mat:
        m = []
        for j in mat:
            si = wn.wup_similarity(i,j)
            if(si == None):
                continue
            if(si > thres):
                m.extend((i,j))
        l.append(m)
    return l

S = sim(vocab)

#List of non-empty clusters

S1 = []
for i in S:
    if len(set(i)) >= 1:
        S1.append(list(set(i)))
       
#Assigning clusters to each word in the vocabulary

dict1 = {}
for i in set(temp_vocab):
    for j in S1:
        for k in j:
            if(i in k.lemma_names()):
                dict1[i] = sorted(list(set(j)))

#Combining words with same clusters

dict2 = {}
for key, value in dict1.items():
    dict2[tuple(value)] = key

dict1 = {}
for k, v in dict2.items():
    dict1[v] = list(k)

#Extracting the names for each clusters

p = []
q = []
for x, y in dict1.items():
    a = []
    p.append(x)
    for i in y:
        a.append(i.lemma_names())
    q.append(sum(a, []))

r = []
for i in q:
    r.append(sorted(list(set(i))))

t = []
for i in list(dict1.values()):
    z = []
    for j in i:
        z.append(j.name())
    t.append(z)

for i in range(len(r)):
    r[i].append(t[i])

for i in r:
    for j in i:
        if isinstance(j,list):
            for k in j:
                i.append(k)
            i.remove(j)

#Creating a dataframe and displaying the frequency of each cluster

df = pd.DataFrame(columns = ["Word","Frequency","Clusters"])
df["Word"] = p
df["Clusters"] = r

frq = []
for x, y in df.iterrows():
    f = 0
    for i in range(len(y["Clusters"])):
        f += temp_vocab.count(y.Clusters[i])
    frq.append(f)

df["Frequency"] = frq
df = df.sort_values(by = ["Frequency"], ascending = False)

#Writing the final output to a csv file

df.to_csv(r"E:/Work/Machine Learning/Assignments/Assignment 2/Clusters for WUP Sim.csv", sep = ',')
