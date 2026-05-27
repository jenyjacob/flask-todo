import spacy
nlp = spacy.load("en_core_web_sm")

CATEGORIES= {
    "shopping": ["buy", "purchase", "get", "need"],
    "work": ["email", "call", "meeting", "report"],
    "health": ["exercise", "doctor", "medication", "appointment"],
}

def categorize(text):
    doc=nlp(text.lower())
    for token in doc:
        for category, keywords in CATEGORIES.items():
            if token.lemma_ in keywords:
                return category
    return "general"
