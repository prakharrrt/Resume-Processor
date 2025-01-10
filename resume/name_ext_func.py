import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

# Initialize matcher with a vocab
matcher = Matcher(nlp.vocab)

def extract_first_name(resume_text):
    nlp_text = nlp(resume_text)
    
    # First name and Last name are always Proper Nouns
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    
    matcher.add('NAME', [pattern])
    
    matches = matcher(nlp_text)
    
    for match_id, start, end in matches:
        span = nlp_text[start:end]
        # Return only the first token (first name)
        return span[0].text