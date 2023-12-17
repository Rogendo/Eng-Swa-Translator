import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector


def get_lang_detector(nlp, name):
    return LanguageDetector()

# # Load the English language model
nlp = spacy.load("en_core_web_sm")

# # Register the language detection factory
Language.factory("language_detector", func=get_lang_detector)

# # Add the language detection component to the pipeline
nlp.add_pipe('language_detector', last=True)


# Assuming you have a text
text = "Hola, ¿cómo estás?"

# Process the text with spaCy
doc = nlp(text)

# Access the detected language using the doc._.language attribute
detected_language = doc._.language['language']

# Print the detected language
print(f"Detected language: {detected_language}")



