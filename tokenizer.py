import re
from normalizer import normilize
from normalizer import cleanup

def tokenize_by_space(contents):
    tokens = []
    for content in contents:
        tokens.extend(content.split(" "))
    tokens.remove('')
    tokens = list(dict.fromkeys(tokens))
    return tokens

def remove_frequent_tokens(tokens):
    frequent_words = ["در", "برای", "چون", "است", "مانند", "باید", "به", "با", "از", "بی", "تا"]
    for word in frequent_words:
        tokens.remove(word)
    return tokens

def simple_tokenize(contents):
    contents = cleanup(contents)
    tokens = tokenize_by_space(contents)
    tokens = remove_frequent_tokens(tokens)
    return tokens

def pro_tokenizer(contents):
    contents = cleanup(contents)
    contents = normalize(contents)

def tokenize(tokenizer_type, contents):
    if tokenizer_type == 'simple':
        return simple_tokenize(contents)
    elif tokenizer_type == 'pro':
        return pro_tokenizer(contents)