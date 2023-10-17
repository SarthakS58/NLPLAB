import spacy
raw_text="""Kabaddi is a contact team sport played between two teams of seven players, originating from India.
It is popular in the Indian subcontinent and other surrounding Asian countries. Although accounts of kabaddi
appear in the histories of ancient India, the game was popularised as a competitive sport in the 
20th century. It is the national sport of Bangladesh. It is the state game of the Indian states of
Andhra Pradesh, Bihar, Chhattisgarh, Haryana, Karnataka, Kerala, Maharashtra, Punjab, Telangana."""
NER = spacy.load("en_core_web_sm", disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])
text= NER(raw_text)
for w in text.ents:
    print(w.text,w.label_)
#spacy.displacy.render(text, style="ent",jupyter=True)

#Output-
#Kabaddi ORG
#between two CARDINAL
#seven CARDINAL
#India GPE
#Indian NORP
#Asian NORP
#India GPE
#the 
#0th century DATE
#Bangladesh GPE
#Indian NORP
#ndhra Pradesh ORG
#Bihar GPE
#Chhattisgarh GPE
#aryana GPE
#Karnataka GPE
#Kerala GPE
#Punjab NORP
#Telangana GPE

