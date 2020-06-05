import re
from normalizer import normilize
from normalizer import cleanup
import os

def tokenize_by_space(contents):
    tokens = []
    for content in contents:
        tokens.append(content.split(" "))
    for t in tokens:
        if ' ' in t:
            t.remove(' ')
        if '' in t:
            t.remove('')
        t = list(dict.fromkeys(t))
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
        if len(arr[0].strip().split()) > 1:
            verbDic.append(arr[0].strip())
    return verbDic

def tokenize_look_ahead(contents):
    verbDic = generate_verb_dictionary()
    nounDic = ['بنا بر این', 'بنابر این','بنا براین', 'ثبت نام','چنان چه', 'مع ذلک',
    'هم چنین', 'تازه وارد','غیر ممکن', ' خوش حال','هیچ کدام', 'آن گونه',' هم اتاقی',
    'به صورت','بی توجهی','به خاطر','نا آشنا', 'سر و صدا','تخت خواب', 'علی الخصوص',
    'مع هذا', 'به ناچار','گه گاه', 'هیئت مدیره','امیر کبیر', 'توافق نامه']
    farDic = verbDic + nounDic
    plural_and_the_boys = ["ها", "تر", "ترین", "ام", "ات", "اش"]
    tokens = []
    for i in range(len(contents)):
        tokens.append([])
        words = contents[i].split()
        j = 0
        while j < len(words):
            if j < len(words) - 2:
                if words[j] + ' ' + words[j + 1] + ' ' + words[j + 2] in farDic:
                    tokens[i].append(words[j] + ' ' + words[j + 1] + ' ' + words[j + 2])
                    j+=2
                elif words[j] + ' ' + words[j + 1] in farDic:
                    tokens[i].append(words[j] + ' ' + words[j + 1])
                    j+=1
                elif words[j + 1] in plural_and_the_boys:
                    tokens[i].append(words[j] + ' ' + words[j + 1])
                    j+=1
                else:
                    tokens[i].append(words[j])
                j+=1
            elif j < len(words) - 1:
                if words[j] + ' ' + words[j + 1] in farDic:
                    tokens[i].append(words[j] + ' ' + words[j + 1])
                    j+=1
                elif words[j + 1] in plural_and_the_boys:
                    tokens[i].append(words[j] + ' ' + words[j + 1])
                    j+=1
                else:
                    tokens[i].append(words[j])
                j+=1
            else:
                tokens[i].append(words[j])
                j+=1
    return tokens

def remove_frequent_tokens(tokens):
    frequent_words = ["در", "برای", "چون", "است", "مانند", "باید", "به", "با", "از", "بی", "تا"]
    for i in range(len(tokens)):
        for word in frequent_words:
            if word in tokens[i]:
                tokens[i].remove(word)
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