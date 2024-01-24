from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# translator pipeline for english to swahili translations

def translate_text_eng_swa(text):
    eng_swa_tokenizer = AutoTokenizer.from_pretrained("../model/eng_swa_model/")
    eng_swa_model = AutoModelForSeq2SeqLM.from_pretrained("../model/eng_swa_model/")



    eng_swa_translator = pipeline(
    "text2text-generation",
    model=eng_swa_model,
    tokenizer=eng_swa_tokenizer,
    )

    translated_text = eng_swa_translator(text, max_length=128, num_beams=5)[0]['generated_text']
    return translated_text

# translator pipeline for swahili to english translations

def translate_text_swa_eng(text):
    swa_eng_tokenizer = AutoTokenizer.from_pretrained("../model/swa_eng_model/")
    swa_eng_model = AutoModelForSeq2SeqLM.from_pretrained("../model/swa_eng_model/")

    swa_eng_translator = pipeline(
    "text2text-generation",
    model=swa_eng_model,
    tokenizer=swa_eng_tokenizer,
    )

    translated_text = swa_eng_translator(text, max_length=128, num_beams=5)[0]['generated_text']
    return translated_text
















# translator pipeline for english to french translations
# english to french




def translate_text_eng_fr(text):
    eng_fr_tokenizer = AutoTokenizer.from_pretrained("../model/en_fr_model/")
    eng_fr_model = AutoModelForSeq2SeqLM.from_pretrained("../model/en_fr_model/")

    eng_fr_translator = pipeline(
        "text2text-generation",
        model=eng_fr_model,
        tokenizer=eng_fr_tokenizer,

    )

    translated_text = eng_fr_translator(text, max_length=128, num_beams=5)[0]['generated_text']
    return translated_text



# text="he is a big man, he can make his own choices"
# translated_text=translate_text_eng_fr(text)
# print(translated_text)

# french to English



def translate_text_fr_eng(text):
    fr_eng_tokenizer =  AutoTokenizer.from_pretrained("./model/fr_en_model")
    fr_eng_model = AutoModelForSeq2SeqLM.from_pretrained("./model/fr_en_model")

    fr_eng_translator = pipeline(
    "text2text-generation",
    model=fr_eng_model,
    tokenizer=fr_eng_tokenizer,

    )

    translated_text = fr_eng_translator(text, max_length=128, num_beams=5)[0]['generated_text']
    return translated_text



text="Je m'apelle Peter Rogendo, et toi?"
translated_text=translate_text_fr_eng(text)
print(translated_text)



# # is_translation_correct=bool

# while True:
#     try:
#         is_translation_correct = input("Is translation correct? ")
#         # is_translation_correct = bool(is_translation_correct)
#         if is_translation_correct=='yes': # If is_translation_correct is True
#             break
#         elif  is_translation_correct=='no': # If is_translation_correct is False
#             print("Translation not correct")
#     except ValueError:
#         print("Invalid input, please enter true or false")



# import pickle
# from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
# # Replace 'your_model.pkl' with the path to your .pkl model file
# with open('../model/model.pkl', 'rb') as file:
#     loaded_model = pickle. load(file)
    
# class CustomSeq2SeqModel:
#     def __init__(self, model):
#         self.model = model

#     def generate(self, input_text, max_length, num_beams):
#         return self.model.generate(input_text, max_length=max_length, num_beams=num_beams, no_repeat_ngram_size=2)

# # Create an instance of the custom model class
# custom_model = CustomSeq2SeqModel(loaded_model)
# tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-swc")
# translator = pipeline(
#     "text2text-generation",
#     model=custom_model,
#     tokenizer=tokenizer,
# )
# def translate_text(text):
#     translated_text = translator(text, max_length=128, num_beams=5)[0]['generated_text']
#     return translated_text

# text="he is a big man, he can make his own choices"
# translate_text(text)
