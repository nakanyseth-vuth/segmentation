# KNLP | BI-LSTM Word Segmentation and POS Tagging tool

> **bilstm_tokenizer** is used for tokenizing text file or input sentences.
> _tokenize_file_bilstm_ is for tokenizing text file and tokenize_sentences_bilstm is for tokenizing input sentences.

---

## Installation

```shell
git clone https://github.com/nakanyseth-vuth/segmentation.git
cd segmentation
pip install -r requirements.txt
```

## Usage :open_mouth: :key:

Import the funtions to your code:

```python
from bilstm_tokenizer import tokenize_sentences_bilstm, tokenize_file_bilstm

input_sents = ["ខ្ញុំទៅសាលា", "សាលារៀនខ្ញុំនៅព្រែកលាប។"]
res = tokenize_sentences_bilstm(input_sents)

print(res)
```

## To include POS Tagging in the results: :sunglasses:

Replace the below code from:

```python
seq,pos = decode(pred_sent, lines[i])
result = [s for s in seq ]
```

to this:

```python
seq,pos = decode(pred_sent, lines[i])
result = [s+"/"+p for s,p in zip(seq,pos) ]
```

@Created by Nakanyseth VUTH
