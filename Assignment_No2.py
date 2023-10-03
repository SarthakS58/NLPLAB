# Assignment No_02
# Name:Sarthak Shinde
# Roll No: 57
# Batch :B3
# Title: "Implementation of Bag of Words using Gensim"

# importing libraries
import gensim
from gensim.matutils import np
from gensim.utils import simple_preprocess
from gensim import corpora, models

# get input
inp = ["""Data science combines math and statistics, 
       specialized programming, advanced analytics
       , artificial intelligence (AI), and machine learning with specific subject 
       matter expertise to uncover actionable insights hidden in an organization's data."""]

# tokens from input
tokens = []
for line in inp[0].split('.'):
    tokens.append(simple_preprocess(line, deacc=True))

# store into g_dict
g_dict = corpora.Dictionary(tokens)

# Count number of tokens
print("The dictionary has: " + str(len(g_dict)) + " tokens")
print(g_dict.token2id)
print("\n")

# Bag of Words
bow =[g_dict.doc2bow(t, allow_update = True) for t in tokens]
print("Bag of Words : ", bow)

#Output::

#The dictionary has: 28 tokens
#{'actionable': 0, 'advanced': 1, 'ai': 2, 'an': 3, 'analytics': 4, 'and': 5, 
# 'artificial': 6, 'combines': 7, 'data': 8, 'expertise': 9, 'hidden': 10, 'in': 11,
#  'insights': 12, 'intelligence': 13, 'learning': 14, 'machine': 15, 'math': 16,
#  'matter': 17, 'organization': 18, 'programming': 19, 'science': 20, 'specialized': 21,
#  'specific': 22, 'statistics': 23, 'subject': 24, 'to': 25, 'uncover': 26, 'with': 27}


#Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 2), (6, 1), (7, 1), (8, 2),
#  (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1),
#  (19, 1), (20, 1), (21, 1), (22, 1), (23, 1), (24, 1), (25, 1), (26, 1), (27, 1)], []]

_dict = corpora.Dictionary([simple_preprocess(line) for line in inp])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in inp]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

print("TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])

#Output :
#Dictionary : 

#[['actionable', 1], ['advanced', 1], ['ai', 1], ['an', 1], ['analytics', 1], ['and', 2], ['artificial', 1], 
# ['combines', 1], ['data', 2], ['expertise', 1], ['hidden', 1], ['in', 1], ['insights', 1], 
# ['intelligence', 1], ['learning', 1], ['machine', 1], ['math', 1], ['matter', 1], ['organization', 1], 
# ['programming', 1], ['science', 1], ['specialized', 1], ['specific', 1], ['statistics', 1], 
# ['subject', 1], ['to', 1], ['uncover', 1], ['with', 1]]
#TF-IDF Vector:

#[['actionable', 0.17], ['advanced', 0.17], ['ai', 0.17], ['an', 0.17], ['analytics', 0.17], ['and', 0.34], 
# ['artificial', 0.17], ['combines', 0.17], ['data', 0.34], ['expertise', 0.17], ['hidden', 0.17], ['in', 0.17],
#  ['insights', 0.17], ['intelligence', 0.17], ['learning', 0.17], ['machine', 0.17], ['math', 0.17], 
# ['matter', 0.17], ['organization', 0.17], ['programming', 0.17], ['science', 0.17], ['specialized', 0.17], 
# ['specific', 0.17], ['statistics', 0.17], ['subject', 0.17], ['to', 0.17], ['uncover', 0.17], ['with', 0.17]]