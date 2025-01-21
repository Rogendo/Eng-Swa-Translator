"""
    main.py


    If training the model proves to be too much for you either computationally, or timewise, You can utilise the deployed version of the model in huggingface
    through the code provided below in the 'main.py' file  Example usage from the deployed model in huggingface. Happy coding! 
    
"""
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


eng_swa_tokenizer = AutoTokenizer.from_pretrained("Rogendo/en-sw")
eng_swa_model = AutoModelForSeq2SeqLM.from_pretrained("Rogendo/en-sw")

eng_swa_translator = pipeline(
    "text2text-generation",
    model = eng_swa_model,
    tokenizer = eng_swa_tokenizer,
)




swa_eng_tokenizer = AutoTokenizer.from_pretrained("Rogendo/sw-en")
swa_eng_model = AutoModelForSeq2SeqLM.from_pretrained("Rogendo/sw-en")

swa_eng_translator = pipeline(
    "text2text-generation",
    model = swa_eng_model,
    tokenizer = swa_eng_tokenizer,
)

def translate_text_swa_eng(text):
  translated_text = swa_eng_translator(text,max_length=128, num_beams=5)[0]['generated_text']
  return translated_text

def translate_text_eng_swa(text):
    translated_text = eng_swa_translator(text, max_length=128, num_beams=5)[0]['generated_text']
    return translated_text

text = "Ninampenda sana mama yangu, bila yeye singekuwa mahali nilipo sasa"
translate_text_swa_eng(text)

text = "My name is John, I love Food so much that I can let it kill me if it had hands of its own"
translate_text_eng_swa(text)