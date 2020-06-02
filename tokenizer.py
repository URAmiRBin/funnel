import re

def cleanup(contents):
    for i in range(len(contents)):
        contents[i] = re.sub('<.*?>', ' ', contents[i])
        contents[i] = re.sub('\u200c', ' ', contents[i])
        contents[i] = re.sub('\n', ' ', contents[i])
        contents[i] = re.sub(r'\&.+;', ' ',contents[i])
        contents[i] = re.sub('[؟.)():!/،,;۲۶۷۵۰۳۴۸۱۹]', '', contents[i])
        contents[i] = re.sub(' +', ' ', contents[i])
    return contents

def simple_tokenize(contents):
    tokens = []
    prep_contents = cleanup(contents)
    for content in contents:
        tokens.extend(content.split(" "))
    tokens.remove('')
    tokens = list(dict.fromkeys(tokens))
    return tokens

def tokenize(tokenizer_type, contents):
    if tokenizer_type == 'simple':
        return simple_tokenize(contents)