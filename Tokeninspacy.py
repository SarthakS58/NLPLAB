import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
"want to finish off this essay before I go to bed."
"His essay was full of spelling errors."
"Have you given that essay in yet?"
)
about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)