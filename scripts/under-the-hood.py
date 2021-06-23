from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

model_name = 'distilbert-base-uncased-finetuned-sst-2-english'

tf_model = TFAutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

text_1 = input("Enter sentence 1: ")
text_2 = input("Enter sentence 2: ")
text_batch = [text_1, text_2]

# tokenizing the sentence
tokens = tokenizer(
    text_batch,
    padding=True,
    truncation=True,
    max_length=512,
    return_tensors='tf' # or it can be 'pt' to return pytorch tensors
)
# printing tokens
print(tokens)

# reversing/decoding tokens to sentences
decoded_tokens = []
for sent in tokens['input_ids']:
    decoded_tokens.append(tokenizer.decode(sent))
# printing reversed tokens
print(decoded_tokens)