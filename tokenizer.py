import re
from normalizer import normilize
from normalizer import cleanup
import os

def tokenize_by_space(contents):
    tokens = []
    for content in contents:
        tokens.extend(content.split(" "))
    tokens.remove('')
    tokens = list(dict.fromkeys(tokens))
    return tokens

def generate_verb_dictionary():
    verbDic = []
    result = []
    resourceName = os.path.dirname(__file__) + "/PersianStemmerLib/data/VerbList.fa"
    with open(resourceName, 'r', encoding="utf-8") as reader:
        result = [line.strip("\r\n ") for line in reader if line.strip("\r\n ")]
    lines = result
    for line in lines:
        arr = line.split("\t")
        verbDic.append(arr[0].strip())
    return verbDic

def tokenize_look_ahead(contents):
    verbDic = generate_verb_dictionary()
    plural_and_the_boys = ["ها", "تر", "ترین", "ام", "ات", "اش"]
    tokens = []
    for i in range(len(contents)):
        words = contents[i].split()
        j = 0
        while j < len(words):
            if j < len(words) - 2:
                if words[j] + ' ' + words[j + 1] + ' ' + words[j + 2] in verbDic:
                    tokens.append(words[j] + ' ' + words[j + 1] + ' ' + words[j + 2])
                    j+=2
                elif 
                elif words[j] + ' ' + words[j + 1] in verbDic:
                    tokens.append(words[j] + ' ' + words[j + 1])
                    j+=1
                elif words[j + 1] in plural_and_the_boys:
                    tokens.append(words[j] + ' ' + words[j + 1])
                    j+=1
                else:
                    tokens.append(words[j])
                j+=1
            elif j < len(words) - 1:
                if words[j] + ' ' + words[j + 1] in verbDic:
                    tokens.append(words[j] + ' ' + words[j + 1])
                    j+=1
                elif words[j + 1] in plural_and_the_boys:
                    tokens.append(words[j] + ' ' + words[j + 1])
                    j+=1
                else:
                    tokens.append(words[j])
                j+=1
            else:
                tokens.append(words[j])
                j+=1
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
    tokens = tokenize_look_ahead(contents)
    tokens = remove_frequent_tokens(tokens)
    return tokens

def tokenize(tokenizer_type, contents):
    if tokenizer_type == 'simple':
        return simple_tokenize(contents)
    elif tokenizer_type == 'pro':
        return pro_tokenizer(contents)