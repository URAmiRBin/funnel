import re
from normalizer import normilize

def cleanup(contents):
    for i in range(len(contents)):
        contents[i] = re.sub('<.*?>', ' ', contents[i])
        contents[i] = re.sub('\u200c', ' ', contents[i])
        contents[i] = re.sub('\u200f', ' ', contents[i])
        contents[i] = re.sub('\n', ' ', contents[i])
        contents[i] = re.sub(r'\&.+;', ' ',contents[i])
        contents[i] = re.sub('[؟.)();:!/،,;۲۶۷۵۰۳۴۸۱۹؛1234567890]', '', contents[i])
        contents[i] = re.sub(' +', ' ', contents[i])
    return contents

def simple_tokenize(contents):
    tokens = []
    prep_contents = cleanup(contents)
    for content in contents:
        tokens.extend(content.split(" "))
    tokens.remove('')
    tokens = list(dict.fromkeys(tokens))
    frequent_words = ["در", "برای", "چون", "است", "مانند", "باید", "به", "با", "از", "بی", "تا"]
    for word in frequent_words:
        tokens.remove(word)
    return tokens

def pro_tokenizer(contents):
    contents = cleanup(contents)
    normal_contents = normalize(contents)

def tokenize(tokenizer_type, contents):
    if tokenizer_type == 'simple':
        return simple_tokenize(contents)
    elif tokenizer_type == 'pro':
        return pro_tokenizer(contents)