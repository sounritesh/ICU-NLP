from transformers import pipeline

# direct web implementation (example task - sentiment analysis)
## only defining the task will get the default model for that task
model_name='nlptown/bert-base-multilingual-uncased-sentiment'
classifier_default = pipeline('sentiment-analysis')
classifier_specific = pipeline('sentiment-analysis', model=model_name)


text = input("Enter a sentence: ")
print(classifier_default(text))
print(classifier_specific(text))