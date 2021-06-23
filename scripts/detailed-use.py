from transformers import pipeline, AutoTokenizer, TFAutoModelForSequenceClassification

model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForSequenceClassification.from_pretrained(model_name, from_pt=True)
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

text = input("Enter a sentence: ")
print(classifier(text))