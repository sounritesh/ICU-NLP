from transformers import pipeline

# direct web implementation (example task - sentiment analysis)
## only defining the task will get the default model for that task
classifier_web = pipeline('sentiment-analysis')

def main():
    text = input("Enter a sentence: ")
    print(classifier_web(text))

if __name__=="__main__":
    main()