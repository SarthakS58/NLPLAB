import spacy
nlp = spacy.load("en_core_web_sm")
conference_help_text = (
    "want to finish off this essay before I go to bed."
"His essay was full of spelling errors."
"Have you given that essay in yet?."
)
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")
        