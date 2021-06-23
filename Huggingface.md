# Huggingface
*official page: https://huggingface.co/*

### installation
*pip install transformers*

### implementation
#### pipeline (module in transformers)
Two things get loaded when importing **pipeline**
- It helps to call pre-trained models like GPT-2, GPT-3, BERT, etc.

**Call:**
*classifier = pipeline(task_name, model_name, tokenizer)* 

**Parameters:**
1. task_name - name of the task e.g. sentiment-analysis 
	- details can be found at: https://huggingface.co/transformers/task_summary.html
2. model - name of the model to be used.
	- available models: https://huggingface.co/models
3. tokenizer - tokenizer used for text pre-processing
	- available tokenizers - https://huggingface.co/transformers/tokenizer_summary.html

#### NOTE: Directly importing from the web is not very suitable more often than not, that is why, we import from local. For local implementation a local path for model parameter can be given for a downloaded model.

#### Detailed implementation
import **AutoTokenizer** (detects the tokenizer of the model automatically) and **TFAutoModelForSequenceClassification** (auto detects the tf model to use)
{These are valid for direct implementation as well}

*the **.from_pretrained(model_name)** returns the model/tokenizer/other class detected automatically*

### Source Code examples
[Krish Naik's Google Collab Notebook (Quickstart)](https://colab.research.google.com/drive/1xyaAMav_gTo_KvpHrO05zWFhmUaILfEd?usp=sharing#scrollTo=qmGhgkHyJnr0)
***direct implementation: [[direct-use.py]]***
***detailed implementation: [[detailed-use.py]]***
***under the hood implementation: [[under-the-hood.py]]***

### Fine tuning a pre-trained model on custom data set
