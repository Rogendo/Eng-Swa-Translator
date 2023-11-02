from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

model_checkpoint = "Helsinki-NLP/opus-mt-en-swc"
tokenizer = AutoTokenizer.from_pretrained("../model/")
model = AutoModelForSeq2SeqLM.from_pretrained("../model/")

translator = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
)

def translate_text(text):
    translated_text = translator(text, max_length=128, num_beams=5)[0]['generated_text']
    return translated_text
