import re

def normilize(contents):
    for i in range(len(contents)):
        contents[i] = re.sub('ك', 'ک', contents[i])
        contents[i] = re.sub('ي', 'ی', contents[i])
        contents[i] = re.sub('ة', 'ه', contents[i])
        contents[i] = re.sub('ؤ', 'و', contents[i])
        contents[i] = re.sub('أ', 'ا', contents[i])
        contents[i] = re.sub('ؤ', 'و', contents[i])
        freaking_erab =     ['\u064B',
                            '\u064C',
                            '\u064D',
                            '\u064E',
                            '\u064F',
                            '\u0650',
                            '\u0651',
                            '\u0652']
        rx = '[' + re.escape(''.join(freaking_erab)) + ']'
        contents[i] = re.sub(rx, '', contents[i])
    return contents

def cleanup(contents):
    for i in range(len(contents)):
        contents[i] = re.sub('<.*?>', ' ', contents[i])
        contents[i] = re.sub('\u200f', ' ', contents[i])
        contents[i] = re.sub('\n', ' ', contents[i])
        contents[i] = re.sub(r'\&.+;', ' ',contents[i])
        contents[i] = re.sub('[؟.)();:!/،,;۲۶۷۵۰۳۴۸۱۹؛1234567890]', '', contents[i])
        contents[i] = re.sub('\u200c', ' ', contents[i])
        contents[i] = re.sub(' +', ' ', contents[i])
    return contents