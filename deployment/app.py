from flask import Flask, render_template,request,jsonify
from flask_socketio import SocketIO, emit
# from deployment.translator import translate_text_eng_swa, translate_text_swa_eng
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



# French to English



def translate_text_fr_eng(text):
    fr_eng_tokenizer =  AutoTokenizer.from_pretrained("../model/fr_en_model")
    fr_eng_model = AutoModelForSeq2SeqLM.from_pretrained("../model/fr_en_model")

    fr_eng_translator = pipeline(
    "text2text-generation",
    model=fr_eng_model,
    tokenizer=fr_eng_tokenizer,

    )

    translated_text = fr_eng_translator(text, max_length=128, num_beams=5)[0]['generated_text']
    return translated_text




# this handles language detection
import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector


# Language detector
def get_lang_detector(nlp, name):
    return LanguageDetector()

# # Load the English language model
nlp = spacy.load("en_core_web_sm")

# # Register the language detection factory
Language.factory("language_detector", func=get_lang_detector)

# # Add the language detection component to the pipeline
nlp.add_pipe('language_detector', last=True)




app = Flask(__name__)

app.config['SECRET_KEY'] = 'qwerty4578'

app = Flask(__name__, static_folder='static')
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template('chat.html')


@socketio.on('message')
def handle_message(message):

    # language detection
    doc=nlp(message)
    detected_language = doc._.language['language']
    print(f"Detected language: {detected_language}")   

    if detected_language=="en":   
        translated_text=translate_text_eng_swa(message)
        print(translate_text_eng_swa(message))
   
    elif detected_language=='fr':
        translated_text=translate_text_fr_eng(message)
        print(translate_text_fr_eng(message))

    elif detected_language=='sw':
        translated_text=translate_text_swa_eng(message)
        print(translate_text_swa_eng(message))
    else:
        translated_text="Sorry, I can't translate that"
        print("Sorry, I can't translate that")
    


    data = {
        'original': message,
        'translated': translated_text
    }
    emit('message', data, broadcast=True)
    
@socketio.on('eng_message')

# API endpoints

@app.route('/translate/en-sw', methods=['POST'])
def translate_en_sw():
    data = request.get_json()
    text_to_translate = data.get('text')
    translated_text = translate_text_eng_swa(text_to_translate)
    return jsonify({'translation': translated_text})

@app.route('/translate/sw-en', methods=['POST'])
def translate_sw_en():
    data = request.get_json()
    text_to_translate = data.get('text')
    translated_text = translate_text_swa_eng(text_to_translate,)
    return jsonify({'translation': translated_text})

@app.route('/api')
def api():
    return render_template('api.html')

if __name__ == '__main__':
    socketio.run(app)
