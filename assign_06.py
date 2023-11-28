#Name- Sarthak Shinde
#Batch -B3
#Roll no- 57
#Assignment Name- Assignment on dependency parsing

import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
piano_text = "A Game of Thrones is the first novel in A Song of Ice and Fire, a series of fantasy novels by American author George R. R. Martin."
piano_doc = nlp(piano_text)
for token in piano_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )
displacy.serve(piano_doc, style="dep")

#output-

'''TOKEN: A
=====
token.tag_ = 'DT'
token.head.text = 'Game'
token.dep_ = 'det'

TOKEN: Game
=====
token.tag_ = 'NNP'
token.head.text = 'is'
token.dep_ = 'nsubj'

TOKEN: of
=====
token.tag_ = 'IN'
token.head.text = 'Game'
token.dep_ = 'prep'

TOKEN: Thrones
=====
token.tag_ = 'NNP'
token.head.text = 'of'
token.dep_ = 'pobj'

TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'is'
token.dep_ = 'ROOT'

TOKEN: the
=====
token.tag_ = 'DT'
token.head.text = 'novel'
token.dep_ = 'det'

TOKEN: first
=====
token.tag_ = 'JJ'
token.head.text = 'novel'
token.dep_ = 'amod'

TOKEN: novel
=====
token.tag_ = 'NN'
token.head.text = 'is'
token.dep_ = 'attr'

TOKEN: in
=====
token.tag_ = 'IN'
token.head.text = 'novel'
token.dep_ = 'prep'

TOKEN: A
=====
token.tag_ = 'DT'
token.head.text = 'Song'
token.dep_ = 'det'

TOKEN: Song
=====
token.tag_ = 'NNP'
token.head.text = 'in'
token.dep_ = 'pobj'

TOKEN: of
=====
token.tag_ = 'IN'
token.head.text = 'Song'
token.dep_ = 'prep'

TOKEN: Ice
=====
token.tag_ = 'NNP'
token.head.text = 'of'
token.dep_ = 'pobj'

TOKEN: and
=====
token.tag_ = 'CC'
token.head.text = 'Ice'
token.dep_ = 'cc'

TOKEN: Fire
=====
token.tag_ = 'NNP'
token.head.text = 'Ice'
token.dep_ = 'conj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'Song'
token.dep_ = 'punct'

TOKEN: a
=====
token.tag_ = 'DT'
token.head.text = 'series'
token.dep_ = 'det'

TOKEN: series
=====
token.tag_ = 'NN'
token.head.text = 'Song'
token.dep_ = 'appos'

TOKEN: of
=====
token.tag_ = 'IN'
token.head.text = 'series'
token.dep_ = 'prep'

TOKEN: fantasy
=====
token.tag_ = 'NN'
token.head.text = 'novels'
token.dep_ = 'compound'

TOKEN: novels
=====
token.tag_ = 'NNS'
token.head.text = 'of'
token.dep_ = 'pobj'

TOKEN: by
=====
token.tag_ = 'IN'
token.head.text = 'novels'
token.dep_ = 'prep'

TOKEN: American
=====
token.tag_ = 'JJ'
token.head.text = 'author'
token.dep_ = 'amod'

TOKEN: author
=====
token.tag_ = 'NN'
token.head.text = 'Martin'
token.dep_ = 'compound'

TOKEN: George
=====
token.tag_ = 'NNP'
token.head.text = 'Martin'
token.dep_ = 'compound'

TOKEN: R.
=====
token.tag_ = 'NNP'
token.head.text = 'Martin'
token.dep_ = 'compound'

TOKEN: R.
=====
token.tag_ = 'NNP'
token.head.text = 'Martin'
token.dep_ = 'compound'

TOKEN: Martin
=====
token.tag_ = 'NNP'
token.head.text = 'by'
token.dep_ = 'pobj'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'is'
token.dep_ = 'punct'

Using the 'dep' visualizer
Serving on http://0.0.0.0:5000 ...'''